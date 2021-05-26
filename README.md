# SHIVA-Smart-Helmet-for-Impaired-Vision-Assistance
This project aims to utilize the technology of Object Detection combined with voice assistant features for visually impaired people which can help them reach their destination and also help them to read sign boards using Computer Vision. This project proposes to build a prototype that performs real time object detection using deep neural network model, YOLOV3. Further the object, and the class of the object is prompted through speech stimulus to the blind person. Along with this we are augmenting a voice assistant for frequent requirements and utilities such as sending emails, getting information over internet, etc. This work uses a combination of YOLOv3 on pretrained dataset and darknet detection framework to build rapid real time multi object detection for a compact, portable and minimal response time device construction. Several prototypes and models have been made keeping in mind the blind people having different usages such as Object Recognizer for the Blind, Visual Aid for the Blind, Google Lookup, etc. Among these technologies, we want to create a computer vision assisted solution keeping in mind their needs and their movements. Computer Vision based solutions are emerging as one of the most promising options due to their affordability and accessibility. This project proposes a system for visually impaired people. The proposed project aims to create a wearable visual aid for visually impaired people.
This repository contains code for a object detector based on YOLOv3: An Incremental Improvement, implementedin PyTorch. The code is based on the official code of YOLO v3, as well as a PyTorch port of the original code, by marvis. One of the goals of this code is to improve upon the original port by removing redundant parts of the code (The official code is basically a fully blown deep learning library, and includes stuff like sequence models, which are not used in YOLO). I've also tried to keep the code minimal, and document it as well as I can.

## Tutorial for building this detector from scratch
If you want to understand how to implement this detector by yourself from scratch, then you can go through this very detailed 5-part tutorial series on Paperspace. Perfect for someone who wants to move from beginner to intermediate pytorch skills.

[Implement YOLO v3 from scratch](https://blog.paperspace.com/how-to-implement-a-yolo-v3-object-detector-from-scratch-in-pytorch-part-1/)

As of now, the code only contains the detection module, but you should expect the training module soon. :)

## Requirements

1. Python 3.5
2. OpenCV
3. PyTorch 0.4

## Add the yolo.weights file

Clone, and cd into the repo directory. The first thing you need to do is to get the weights file This time around, for v3, authors has supplied a weightsfile only for COCO [here](https://pjreddie.com/media/files/yolov3.weights), and place the weights file into your repo directory.

## Add the Frozen East Text Detection for OCR
You'll need to download the froxen east text detection in order to perform OCR. you can download it from [here](https://www.kaggle.com/yelmurat/frozen-east-text-detection/download), and place the downloaded file into your repo directory.

## Run the shiva_od.py file
Go to this repo in the terminal and write this command
```
python shiva_od.py 
```
