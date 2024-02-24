import cv2
import numpy as np
import socket
import sys
import pickle
import struct
from picamera2 import Picamera2
import time


# cap.set(cv2.CAP_PROP_FRAME_WIDTH,)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH,480)
clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('192.168.111.241',8009))
# clientsocket.connect(('localhost',8089))
picam2 = Picamera2()
config = picam2.create_preview_configuration({'format': 'RGB888'})
picam2.configure(config)
picam2.start()

while True:
    frame = picam2.capture_array()
    #framef = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    data = pickle.dumps("hi from pi")

    # Send message length first
    message_size = struct.pack("L", len(data)) ### CHANGED

    # Then data
    clientsocket.sendall(message_size + data)
