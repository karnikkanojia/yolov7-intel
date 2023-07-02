# Team Name - Ai Artistss
# Problem Statement - Object Detection For Autonomous Vehicles
## Output Videos From Our Model
https://drive.google.com/drive/folders/1WSYknCyP11lraXsjaTRNCGYYS4ejhJXf
## Introduction
"Enhanced Object Detection with Intel: Leveraging Intel Technologies for Accurate and Efficient YOLOv5 Model"

In our project, we have harnessed the power of Intel technologies to enhance the capabilities of the YOLOv5 algorithm for object detection. By leveraging Intel's optimized libraries and frameworks, such as Intel oneDAL, Intel optimized PyTorch, and the SYCL/DPC++ libraries, we have achieved superior performance, accuracy, and efficiency in our object detection model. This integration enables us to process data faster, optimize resource utilization, and streamline post-processing steps, leading to robust and real-time object detection for autonomous vehicle applications.
## **Table of Contents**
 - Purpose
 - A Brief of the Prototype
 - Architecture Diagram
 - Flow Diagram
 - Expected Input-Output
 - Dataset and Annotations
 - Folder Structure
 - Tech Stack
      - Optimized software components
      - Optimized Solution setup
 - Step-by-Step Code Execution Instructions
      - Installation
 - Overview
      - Training
 - Output Videos From Our Model
 - Output Graph
 - Object Detection for Autonomus vehicles
 - What I Learned

 <!-- Purpose -->
## Purpose
The purpose of our project is to leverage Intel technologies to enhance the YOLOv7 algorithm for object detection in the context of autonomous vehicles. By utilizing Intel oneDAL, Intel optimized PyTorch, and the SYCL/DPC++ libraries with neural compressor, we aim to achieve improved performance, accuracy, and efficiency in detecting and classifying objects in real-time. Our goal is to provide a reliable and effective solution for autonomous vehicles to detect and respond to various objects and obstacles on the road, ensuring enhanced safety and efficiency in autonomous driving systems.

<!-- A Brief of the Prototype -->
## 📜 A Brief of the Prototype:
Our prototype's real-time object detection and distance recognition features are meant to make self-driving cars safer and more efficient. By leveraging the power of Intel technologies and frameworks, we've created a robust system that combines advanced computer vision algorithms and deep learning models.Intel AI Analytics Toolkit, featuring optimised deep learning frameworks like PyTorch, powers the prototype. Intel-optimized libraries like oneDNN and oneDAL were used to train and infer deep learning models. This helps us locate items around the car.

## Core components of oneAPI/SYCL used in the project
- Intel Optimization for PyTorch
  - Gave us extra performance boost on Intel Hardware.
- Intel Neural Compressor
  - Performed post-training quantization using Neural Compressor which helped accelerate the model inference speed and decrease the memory load while still maintaining the model accuracy.
- Intel DevCloud
  - Trained our model and did benchmarking on our dataset in Intel DevCloud

## Architecture – Impact of oneAPI/SYCL (How oneAPI /SYCL helped you?)
![WhatsApp Image 2023-07-02 at 07 40 34](https://github.com/karnikkanojia/yolov7-intel/assets/82893678/035802cb-eef0-4d53-8584-0f0ffd4e0b43)
## INFERENCE TIME COMPARISION WITH IPEX AND WITHOUT IPEX
![Screenshot 2023-07-02 072803](https://github.com/karnikkanojia/yolov7-intel/assets/82893678/98909054-2438-493e-b3fa-0f26a082e88b)

## Metrices
# Object Loss
![ol](https://github.com/karnikkanojia/yolov7-intel/assets/82893678/1ead10a1-35a1-4e29-91dc-23e6d03bcdae)

# Mean Precision Precision
![map](https://github.com/karnikkanojia/yolov7-intel/assets/82893678/08b2bf2e-b452-4f44-a042-b2e28af69473)

# Hyper-parameters
![Hyper-parameters](https://github.com/karnikkanojia/yolov7-intel/assets/82893678/d47322d8-0d2c-4e1d-be37-97b19cb3b3ec)

# what I learned
- Familiarity with YOLO Architecture: YOLO (You Only Look Once) is a popular and efficient object detection algorithm. Implementing YOLOv8 helped us familiarise ourselves with its architecture, including the backbone network (e.g., Darknet), feature extraction layers, and detection layers.

- Preprocessing and Augmentation Techniques: Object detection often requires preprocessing and data augmentation to improve model performance. While implementing YOLOv8, We have learnt about various techniques such as resizing, normalization, data augmentation (e.g., random cropping, flipping), and handling object annotations.
Hyperparameter Tuning: YOLOv8 has several hyperparameters that affect the model's performance, such as learning rate, batch size, anchor sizes, and confidence thresholds.
- We have learnt and gained experience in tuning these hyperparameters to optimize the model's accuracy and efficiency.
We explored a range of Intel's software development tools and libraries, including the AI analytics toolkit and its libraries.
Using Intel® AI Analytics Toolkits we were able to enhance performance speed in training data.
- Brainstormed with novel algorithms for different kinds of object detection specific to autonomous vehicles.Implemented Object detection alongwith distance mapping of nearby objects in order to prevent collisions. We've been able to custom label/annotate the objects in detection.
- We explored a range of Intel's software development tools and libraries, including the AI analytics toolkit and its libraries.
Using Intel® AI Analytics Toolkits we were able to enhance performance speed in training data. Brainstormed with novel algorithms for different kinds of object detection specific to autonomous vehicles. Implemented Object detection alongwith distance mapping of nearby objects in order to prevent collisions.
We've been able to custom label/annotate the objects in detection.






