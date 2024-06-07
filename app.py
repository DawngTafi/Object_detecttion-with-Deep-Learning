from pathlib import Path
from PIL import Image
import streamlit as st

import config
from utils import load_model, infer_uploaded_image, infer_uploaded_video, infer_uploaded_webcam

#Page layout
st.set_page_config(
    page_title="YOLO for Object Detection ",
    page_icon="🤖",
    layout= "wide",
    initial_sidebar_state="expanded" 
    )

#Heading
st.title("Using module YOLO in Deep Learning to Object Detection")

#sidebar
st.sidebar.header("Set Model Config")

#Options model
task_type  = st.sidebar.selectbox(
    "Select Model Task",
    ["Detection Object"]
)

data_type = None
if task_type == "Detection Object":
    data_type = st.sidebar.selectbox(
        "Select Data",
        ["Coco Datasets", "Custom Datasets"]
    )
    
confidence = float(st.sidebar.slider(
    "Select Model Confidence", 30, 100, 50)) / 100

model_type = None
if data_type == "Coco Datasets":
    model_type = st.sidebar.selectbox(
        "Select Model",
        config.DETECTION_MODEL_LIST
    )
    model_path = ""
    if model_type:
        model_path = Path(config.DETECTION_MODEL_DIR, str(model_type))    
    
if data_type == "Custom Datasets":
    model_type = st.sidebar.selectbox(
        "Select Data",
        ["Cat", "Dog", "Key", "Phone"]        
    )
    if model_type == "Cat":
        model_path = Path(config.CAT)
    if model_type == "Dog":
        model_path = Path(config.DOG)
    if model_type == "Key":
        model_path = Path(config.KEY)
    if model_type == "Phone":
        model_path = Path(config.PHONE)         
    

try:
        model = load_model(model_path)
except Exception as e:
        st.error(f"Unable to load model. Please check the specified path: {model_path}")
        
st.sidebar.header("Image/Video Config")
source_selectbox = st.sidebar.selectbox(
    "Select Source",
    config.SOURCES_LIST
)        
source_img = None
if source_selectbox == config.SOURCES_LIST[0]: # Image
    infer_uploaded_image(confidence, model)
elif source_selectbox == config.SOURCES_LIST[1]: # Video
    infer_uploaded_video(confidence, model)
elif source_selectbox == config.SOURCES_LIST[2]: # Webcam
    infer_uploaded_webcam(confidence, model)
else:
    st.error("Currently only 'Image' and 'Video' source are implemented")