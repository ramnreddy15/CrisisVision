import socket
from struct import unpack
import numpy as np
import cv2
from ultralytics import YOLO
import supervision as sv

HOST = '192.168.252.241'
PORT = 8009

model = YOLO("yolov8n.pt")
box_annotator = sv.BoxAnnotator(
    thickness=2,
    text_thickness=2,
    text_scale=1
)
label_annotator = sv.LabelAnnotator()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

s.bind((HOST, PORT))
print('Socket bind complete')
s.listen(10)
print('Socket now listening')

conn, addr = s.accept()
print("Client connected at ", addr)

while(True):
    bs = conn.recv(8)
    (length,) = unpack('>Q', bs)
    data = b''
    while len(data) < length:
        to_read = length - len(data)
        data += conn.recv(4096 if to_read > 4096 else to_read)

    data = np.frombuffer(data, dtype='uint8').reshape((480,640,3))
    data = cv2.rotate(data, cv2.ROTATE_180)
    result = model(data, conf=0.2)[0]
    detections = sv.Detections.from_ultralytics(result)
    labels = [
        model.model.names[class_id]
        for class_id
        in detections.class_id
    ]
    data = box_annotator.annotate(
        scene=data, 
        detections=detections,
        labels=labels
    )
    cv2.imshow('frame', data)
    cv2.waitKey(1)
