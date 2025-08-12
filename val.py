from ultralytics import YOLO
model = YOLO("/home/long/develop/实验/消融实验/yolov8_PConv_SimAM_WIoU/runs/detect/train12/weights/best.pt")
# model.val()
model.val(data='/home/long/develop/实验/yolov8_SimAM_res/yolov8_SimAM/ultralytics/datasets/Helmet.yaml', device='cpu')
