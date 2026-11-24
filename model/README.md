# Trained Model

The trained YOLOv8n road damage detection weights are stored in this folder.

Model file: `best.pt`

Training:
- Epochs: 20
- Image size: 640
- Batch size: 16
- GPU: NVIDIA Tesla T4
- Pretrained initialization: Generic COCO-pretrained YOLOv8n

The model detects longitudinal cracks, transverse cracks, alligator cracks and potholes.

Validation mAP@50: 0.456
Validation mAP@50:95: 0.199
