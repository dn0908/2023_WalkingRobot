from time import time
import torch
import torchvision
import matplotlib.pyplot as plt
import numpy as np
import cv2
from yolov5.models.experimental import attempt_load

# model = attempt_load("./runs/train/exp3/weights/best.pt")
model = torch.hub.load("/home/diana/2023_WalkingRobot", "custom", path="best.pt", source="local")

cap = cv2.VideoCapture(0)
while cap.isOpened():
    start = time()
    ret, frame = cap.read()
    # frame = cv2.resize(frame, ())
    # transform = torchvision.transforms.Compose([torchvision.transforms.ToTensor()])
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = torch.reshape(frame, (1, 3, 640, 640))
    frame = torch.from_numpy(frame).float()
    result = model(frame)
    cv2.imshow('Yolo', np.squeeze(result.render()))
    if cv2.waitKey(5) & 0xff==ord('x'):
        break
    if cv2.getWindowProperty("Yolo", cv2.WND_PROP_VISIBLE)<1:
        break

    end = time()
    fps = 1/(end-start)
    print(fps)

cap.release()
cv2.destroyAllWindows()