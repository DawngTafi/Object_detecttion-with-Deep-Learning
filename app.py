from pathlib import Path
from PIL import Image
import streamlit as st
from utils import train_model

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

model_type = None
if data_type == "Coco Datasets":
    model_type = st.sidebar.selectbox(
        "Select Model",
        ["model 1"]
    ##    config.DETECTION_MODEL_LIST
    )
    
##    model_path = ""
##    if model_type:
##        model_path = Path(config.DETECTION_MODEL_DIR, str(model_type))
    
##    try:
##        model = load_model(model_path)
##    except Exception as e:
##        st.error(f"Unable to load model. Please check the specified path: {model_path}")

#if data_type == "Custom Datasets":
#    model_type = st.sidebar.selectbox(
#        "Model",
    ##    config.DETECTION_MODEL_LIST
#    )
##confidence = float(st.sidebar.slider(
##    "Select Model Confidence", 30, 100, 50)) / 100
