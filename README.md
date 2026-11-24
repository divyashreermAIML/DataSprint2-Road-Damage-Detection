# Anveshan DataSprint 2.0 – Road Damage Detection

## Project Overview
This project uses computer vision and the YOLO object detection framework to identify and localize road damage in road images.

The system detects four categories:

| Class | Description |
|---|---|
| D00 | Longitudinal crack |
| D10 | Transverse crack |
| D20 | Alligator crack |
| D40 | Pothole |

## Model
- Architecture: YOLOv8n
- Framework: Ultralytics
- Pretrained weights: Generic COCO-pretrained YOLOv8n
- Training dataset: Official DataSprint 2.0 competition dataset
- Image size: 640 × 640

## Dataset
The official competition dataset contains training, validation and test images. No external road-damage images or labels are used.

## Evaluation
The competition evaluates:
- mAP@50
- mAP@50:95
- Precision
- Recall
- Inference speed
- Robustness

## Project Status
The model training and inference pipeline are being finalized. Final model metrics and reproducibility instructions will be added after verification.

## Compliance
This project follows the competition restrictions on external data and pretrained weights. The model uses only approved generic pretrained weights and the official competition dataset.

## Team
Anveshan DataSprint 2.0 – Intelligent Road Damage Detection
