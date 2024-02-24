import cv2
import numpy as np
import socket
import struct
import pickle

cap = cv2.VideoCapture(0)
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('192.168.252.241', 5000))  # Replace with your server IP and port
print("connected")

while True:
    ret, frame = cap.read()
    data = pickle.dumps(frame)
    message_size = struct.pack("L", len(data))
    clientsocket.sendall(message_size + data)