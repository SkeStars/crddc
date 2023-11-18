# RDD
# Installation
conda create -n rdd python=3.10.12  
conda activate rdd  
git clone https://github.com/SkeStars/rdd.git
cd rdd 
#cuda >= 11.1  
pip3 install torch==1.8.2+cu111 torchvision==0.9.2+cu111 torchaudio===0.8.2 -f https://download.pytorch.org/whl/lts/1.8/torch_lts.html  
#official yolov5 r6.1  
pip install -r yolov5/requirements.txt  
#official yolov7  
pip install -r yolov7/requirements.txt  
# Quick Start
following ipynb  
# Model
| model | pretrained weight (google drive) | 
| :-----| :---- | 
| YOLOv5x_640 | [YOLOv5x_640] | 
| YOLOv5x6_1280 | [YOLOv5x6_1280] | 
| YOLOv7x_640 | [YOLOv7x_640] | 
# Acknowledgement
- https://github.com/ultralytics/yolov5
- https://github.com/WongKinYiu/yolov7
