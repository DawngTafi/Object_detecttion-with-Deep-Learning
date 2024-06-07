from ultralytics import YOLO
#cat train
data = r'data_custom/Cat/data.yaml'
model = YOLO('yolov8n.pt')
results = model.train(data=data, epochs=10, imgsz=640, project = 'trainmodel', name = 'cat_model')

#dog train
##data = r'data_custom/Dog/data.yaml'
##model = YOLO('yolov8n.pt')
##results = model.train(data=data, epochs=10, imgsz=640, project = 'trainmodel', name = 'dog_model')

#hand train
##data = r'data_custom/Hand/data.yaml'
##model = YOLO('yolov8n.pt')
##results = model.train(data=data, epochs=10, imgsz=640, project = 'trainmodel', name = 'hand_model')

#Key
##data = r'data_custom/Key/data.yaml'
##model = YOLO('yolov8n.pt')
##results = model.train(data=data, epochs=10, imgsz=640, project = 'trainmodel', name = 'key_model')