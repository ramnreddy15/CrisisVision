import cv2
import numpy as np
import socket
import sys
import pickle
import struct
from ultralytics import YOLO
import supervision as sv

model = YOLO("yolov8n.pt")
box_annotator = sv.BoxAnnotator(
    thickness=2,
    text_thickness=2,
    text_scale=1
)
label_annotator = sv.LabelAnnotator()

cap=cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH,)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH,480)
clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('192.168.252.241',8009))
# clientsocket.connect(('localhost',8089))

while True:
    ret,frame=cap.read()
    frame = cv2.resize(frame,(640,480), interpolation=cv2.INTER_LINEAR)
    result = model(frame, conf=0.8)[0]
    # print(result)
    detections = sv.Detections.from_ultralytics(result)
    # print(detections)
    labels = [
        model.model.names[class_id]
        for class_id
        in detections.class_id
    ]

#     labels = [
#         f"{model.model.names[class_id]} {confidence:0.2f}"
#         for confidence, class_id in detections
#    ]
    # Serialize frame
    frame = box_annotator.annotate(
        scene=frame, 
        detections=detections,
        labels=labels
        )
    
    data = pickle.dumps(frame)

    # Send message length first
    message_size = struct.pack("L", len(data)) ### CHANGED

    # Then data
    clientsocket.sendall(message_size + data)
