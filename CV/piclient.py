import cv2
import numpy as np
import socket
import struct
from picamera2 import Picamera2

clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('192.168.111.51',8009))
picam2 = Picamera2()
config = picam2.create_preview_configuration({'format': 'RGB888'})
picam2.configure(config)
picam2.start()

while True:
    frame = picam2.capture_array()
    frameS = frame.tobytes()
    message_size = struct.pack(">Q", len(frameS)) ### CHANGED
    clientsocket.sendall(message_size)
    clientsocket.sendall(frameS)
