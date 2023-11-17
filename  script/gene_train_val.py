import os
import errno
import pwd
images_path = os.path.join('train', 'images')
image_list = os.listdir(images_path)
with open('train.txt', 'a') as f:
    for img in image_list:
        img_path = os.path.join('datasets/', images_path, img)
        if img != '24510-out_ori.jpg':
            f.write(img_path + '\n')
with open('val.txt', 'a') as f:
    img = '24510-out_ori.jpg'
    img_path = os.path.join('datasets/', images_path, img)
    f.write(img_path + '\n')
        