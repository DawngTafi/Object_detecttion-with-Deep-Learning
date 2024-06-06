from ultralytics import YOLO
import cv2

## Train YOLO with custom datasets
datapath = r'data.yml'
model  = YOLO('yolov8n.pt')
model = model.train(data= datapath, epochs = 10,imgsz = 640)

