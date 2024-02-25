import cv2
import numpy as np
import socket
import sys
import json
import struct
from picamera2 import Picamera2
import time


# cap.set(cv2.CAP_PROP_FRAME_WIDTH,)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH,480)
clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('192.168.111.51',8009))
# clientsocket.connect(('localhost',8089))
picam2 = Picamera2()
config = picam2.create_preview_configuration({'format': 'RGB888'})
picam2.configure(config)
picam2.start()
while True:
    frame = picam2.capture_array()
    frameS = json.dumps(frame.tolist()).encode()
    #framef = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    #data = pickle.dumps(frame)
    message_size = struct.pack(">Q", len(frameS)) ### CHANGED
    clientsocket.sendall(message_size)
    clientsocket.sendall(frameS)
