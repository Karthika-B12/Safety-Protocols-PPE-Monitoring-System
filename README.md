# Safety-Protocols-PPE-Monitoring-System

PPE (Personal Protective Equipment) detection is crucial for ensuring safety on construction sites. This project leverages YOLOv8, a state-of-the-art deep learning model, to accurately detect and localize PPE such as helmets, face shields, jackets, dust masks, eye wear, gloves, and protective boots in real time.

Table of Contents:
Introduction
Installation
Dataset
Image & Object Detection
Results
References
Introduction
This project utilizes YOLOv8, an advanced deep learning model with 218 layers and 25.8 million parameters, to detect PPE items on construction sites. YOLOv8's precision and recall metrics, along with its mAP (mean average precision), make it an effective tool for enhancing safety by ensuring workers are properly equipped with necessary protective gear.

Objects Detected
The following PPE items are identified:

Helmets
Face Shields
Jackets
Dust Masks
Eye Wear
Gloves
Protective Boots
Installation
To run this project, you'll need to install several packages and dependencies. Follow the steps below:

Start by cloning the repository and installing the required packages:

   git clone https://github.com/Aadhishreevijay/Safety-Protocols-Personel-Protective-Equipment-PPE-Monitoring-System.git

   cd Safety-Protocols-Personel-Protective-Equipment-PPE-Monitoring-System

   pip install -r requirements.txt
Install Python Packages:

   pip install IPython ultralytics==8.0.0 roboflow
Check NVIDIA GPU (Optional but recommended for faster training):

   !nvidia-smi
Install YOLOv8:

   pip install ultralytics==8.0.0
Set Up Roboflow: It's recommended to copy the Roboflow code instead of downloading the dataset as a folder. When copying the code, make sure it's in YOLOv5 format:

   from roboflow import Roboflow
   rf = Roboflow(api_key="4hIhYKGrnWHaWXRqZsZg")
   project = rf.workspace("objet-detect-yolov5").project("eep_detection-u9bbd")
   dataset = project.version(1).download("yolov5")
Dataset
The dataset used for this project is hosted on Roboflow. You can access and download the dataset from the following link:

EEP Detection Dataset on Roboflow.

For Video & Image Detection
For video detection, use video_detect.py
For image detection, use image_detect.py
Results
Metrics:
Precision: 0.926
Recall: 0.88
mAP (IoU=0.5): 0.91
mAP (0.5:0.95): 0.651
Visual Results:
Below are some visualizations of the model's performance:

Confusion Matrix:

This matrix shows the true positive, false positive, true negative, and false negative rates. image
F1 Curve:

The F1 curve demonstrates the balance between precision and recall. image
Precision-Recall (PR) Curve

This curve shows the trade-off between precision and recall. image
Precision Curve (P)

Precision curve at various thresholds. image
Recall Curve (R)

Recall curve at different confidence thresholds. image
Loss Curves:

image

Sample Image Prediction:

image

image

Recommendation:
If running this on Google Colab, it’s recommended to change the runtime to GPU for faster processing.
Navigate to Runtime -> Change runtime type and select GPU under Hardware accelerator.
Images and Videos are given in images and videos
Find the required weights best.pt, last.pt, yolov8m.py in weights
Reference
Dataset: Roboflow EEP Detect Dataset
Ultralytics Documentation: docs.ultralytics.com
Ultralytics GitHub Repository: github.com/ultralytics/ultralytics
Roboflow Universe: universe.roboflow.com
