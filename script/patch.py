import xml.etree.ElementTree as ET
import os
import cv2
from PIL import Image
import numpy as np
from pathlib import Path
import argparse

# 创建命令行参数解析器
parser = argparse.ArgumentParser()
parser.add_argument('--input', help='Input directory')
parser.add_argument('--output', help='Output directory')
args = parser.parse_args()

output_dir=args.output + "/" + args.input.split('/')[-1] +"_640"
Path(output_dir + "/labels/").mkdir(parents=True, exist_ok=True)
Path(output_dir +"/images/").mkdir(parents=True, exist_ok=True)

List = os.listdir('args.input/labels/')
sorted_List = sorted(List)

def sliding_window(image, stepSize, windowSize):
    for y in range(0, image.shape[0], stepSize):
        if image.shape[0] - y < windowSize[1]*0.7:
            break
        for x in range(0, image.shape[1], stepSize):
            if image.shape[1] - x < windowSize[0]*0.7:
                break
            else:
                yield (x, y, image[y:y + windowSize[1], x:x + windowSize[0]])

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return [x,y,w,h]

for nw in sorted_List:
    imageName = 'args.input/images/' + nw.replace('.txt', '.jpg')
    print(imageName)
    image = cv2.imread(imageName)
#    print(image.shape)
    features = []
    windows = sliding_window(image, 400, (640, 640))
#    windows = sliding_window(image, 400, (1024, 1024))
#    print(len(list(windows)))
    idx = 0
    for window in windows:
#        print(window)
#        print(window[2])
        data = window[2][:,:,::-1]
        img = Image.fromarray(data)
        img.save(output_dir+"/images/" + imageName.split('/')[-1].replace('.jpg', '_') + str(idx) + ".jpg")
        idx += 1

for nw in sorted_List:
    with open(args.input+'/labels/' + nw, 'r') as file:
        lines = file.readlines()

    imageName = args.input+'/images/' + nw.replace('.txt', '.jpg')
    image = cv2.imread(imageName)
    height, width, _ = image.shape

    labelWindowSize = 640
    labelStepSize = 400

    cnt = 0
    for line in lines:
        line = line.strip().split(' ')
        class_name = line[0]
        xmin = float(line[1]) * width
        ymin = float(line[2]) * height
        xmax = float(line[3]) * width
        ymax = float(line[4]) * height

        for x, y, window in sliding_window(image, labelStepSize, (labelWindowSize, labelWindowSize)):
            window_xmin = x
            window_ymin = y
            window_xmax = x + labelWindowSize
            window_ymax = y + labelWindowSize

            if xmin >= window_xmin and ymin >= window_ymin and xmax <= window_xmax and ymax <= window_ymax:
                window_xmin = int(xmin - window_xmin)
                window_ymin = int(ymin - window_ymin)
                window_xmax = int(xmax - window_xmin)
                window_ymax = int(ymax - window_ymin)
                [cx,cy,cw,ch] = convert((labelWindowSize,labelWindowSize), (window_xmin,window_xmax, window_ymin, window_ymax))
                label = f"{class_name} {cx} {cy} {cw} {ch}"
                with open(f"{output_dir}/labels/{nw.split('.')[0]}_{cnt}.txt", "w") as output_file:
                    output_file.write(label)

                cnt += 1
