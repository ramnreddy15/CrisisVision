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

data = b'' ### CHANGED
payload_size = struct.calcsize("L") ### CHANGED

while True:

    # Retrieve message size
    while len(data) < payload_size:
        data += conn.recv(4096)

    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("L", packed_msg_size)[0] ### CHANGED

    # Retrieve all data based on message size
    while len(data) < msg_size:
        data += conn.recv(4096)

    frame_data = data[:msg_size]
    data = data[msg_size:]

    # Extract frame
    frame = pickle.loads(frame_data)

    # Display
    cv2.imshow('frame', frame)
    cv2.waitKey(1)
