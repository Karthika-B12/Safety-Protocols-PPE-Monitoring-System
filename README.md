# Safety-Protocols-PPE-Monitoring-System

PPE (Personal Protective Equipment) detection is crucial for ensuring safety on construction sites. This project leverages YOLOv8, a state-of-the-art deep learning model, to accurately detect and localize PPE such as helmets, face shields, jackets, dust masks, eye wear, gloves, and protective boots in real time.

## Table of Contents
- [Introduction](#introduction)
- [Objects Detected](#objects-detected)
- [Installation](#installation)
- [Dataset](#dataset)
- [Image & Object Detection](#image--object-detection)
- [Results](#results)
- [References](#references)

## Introduction
This project utilizes YOLOv8, an advanced deep learning model with 218 layers and 25.8 million parameters, to detect PPE items on construction sites. YOLOv8's precision and recall metrics, along with its mAP (mean average precision), make it an effective tool for enhancing safety by ensuring workers are properly equipped with necessary protective gear.

## Objects Detected
The following PPE items are identified:
- Helmets
- Face Shields
- Jackets
- Dust Masks
- Eye Wear
- Gloves
- Protective Boots

## Installation
To run this project, you'll need to install several packages and dependencies. Follow the steps below:

1. **Clone the repository and install the required packages:**
   ```bash
   git clone https://github.com/Karthika-B12/Safety-Protocols-PPE-Monitoring-System.git
   cd Safety-Protocols-PPE-Monitoring-System.git
   pip install -r requirements.txt
   ```

2. **Install Python Packages:**
   ```bash
   pip install IPython ultralytics==8.0.0 roboflow
   ```

3. **Check NVIDIA GPU (Optional but recommended for faster training):**
   ```bash
   !nvidia-smi
   ```

4. **Install YOLOv8:**
   ```bash
   pip install ultralytics==8.0.0
   ```

5. **Set Up Roboflow:**  
   It's recommended to copy the Roboflow code instead of downloading the dataset as a folder. When copying the code, make sure it's in YOLOv5 format:
   ```python
   from roboflow import Roboflow
   rf = Roboflow(api_key="4hIhYKGrnWHaWXRqZsZg")
   project = rf.workspace("objet-detect-yolov5").project("eep_detection-u9bbd")
   dataset = project.version(1).download("yolov5")
   ```

## Dataset
The dataset used for this project is hosted on Roboflow. You can access and download the dataset from the following link:

[EEP Detection Dataset on Roboflow](https://universe.roboflow.com/).

## Image & Object Detection
- **For video detection**, use `video_detect.py`
- **For image detection**, use `image_detect.py`

## Results
- **Metrics:**
  - Precision: 0.926
  - Recall: 0.88
  - mAP (IoU=0.5): 0.91
  - mAP (0.5:0.95): 0.651

- **Visual Results:**
  - **Confusion Matrix:**  
    ![Confusion Matrix]![Screenshot 2024-09-03 225911](https://github.com/user-attachments/assets/d3c76ca4-eb67-43db-8382-55951277ef67)
  - **F1 Curve:**  
    ![F1 Curve](path_to_f1_curve_image)
  - **Precision-Recall (PR) Curve:**  
    ![PR Curve](path_to_pr_curve_image)
  - **Precision Curve (P):**  
    ![Precision Curve](path_to_precision_curve_image)
  - **Recall Curve (R):**  
    ![Recall Curve](path_to_recall_curve_image)
  - **Loss Curves:**  
    ![Loss Curves](path_to_loss_curves_image)

- **Sample Image Prediction:**
  ![Sample Prediction 1](path_to_sample_prediction_image_1)
  ![Sample Prediction 2](path_to_sample_prediction_image_2)

## Recommendation
If running this on Google Colab, it’s recommended to change the runtime to GPU for faster processing.
- Navigate to **Runtime -> Change runtime type** and select **GPU** under Hardware accelerator.

Images and videos are provided in the `images` and `videos` directories.  
Find the required weights (`best.pt`, `last.pt`, `yolov8m.py`) in the `weights` directory.

## References
- **Dataset:** [Roboflow EEP Detect Dataset](https://universe.roboflow.com/)
- **Ultralytics Documentation:** [docs.ultralytics.com](https://docs.ultralytics.com)
- **Ultralytics GitHub Repository:** [github.com/ultralytics/ultralytics](https://github.com/ultralytics/ultralytics)
- **Roboflow Universe:** [universe.roboflow.com](https://universe.roboflow.com/)
