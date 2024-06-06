from ultralytics import YOLO
import streamlit as st
import cv2
from PIL import Image
import tempfile

def train_model(data_path):
## Train YOLO with custom datasets
    datapath = r'data.yaml'
# Load a model
    model = YOLO("yolov8n.yaml")  # build a new model from YAML
    model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)
    model = YOLO("yolov8n.yaml").load("yolov8n.pt")  # build from YAML and transfer weights
# Train the model
    results = model.train(data=datapath, epochs=10, imgsz=640)
##Upload model after train  
    modelpath  = r'trainmodel/weights/best.pt'
    model = YOLO(modelpath)
def load_model(model_path):
    mo