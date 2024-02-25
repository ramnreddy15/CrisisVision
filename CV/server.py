import socket
from struct import unpack
import numpy as np
import cv2

HOST = '192.168.111.51'
PORT = 8009

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
    cv2.imshow('frame', data)
    cv2.waitKey(1)
