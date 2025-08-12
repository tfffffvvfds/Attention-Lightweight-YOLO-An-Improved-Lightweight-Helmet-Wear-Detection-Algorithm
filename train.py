from ultralytics import YOLO
import os
# 加载模型
model = YOLO(model="/home/long/develop/实验/yolov8_SimAM_res/yolov8_SimAM/ultralytics/models/v8/yolov8s_SimAM.yaml" )  # 从头开始构建新模型
# model = YOLO("yolov8s.pt")
print(model.model)
# Use the model
results = model.train(data="/home/long/develop/实验/yolov8_SimAM_res/yolov8_SimAM/ultralytics/datasets/Helmet.yaml", epochs=350, device=0 ,batch=8, imgsz=[416,416], workers=8)  # 训练模型