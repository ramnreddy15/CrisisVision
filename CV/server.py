import pickle
import socket
import struct

import cv2

HOST = '192.168.111.241'
PORT = 8009

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

s.bind((HOST, PORT))
print('Socket bind complete')
s.listen(10)
print('Socket now listening')

conn, addr = s.accept()
print("Client connected at ", addr)

sockfile = conn.makefile('rb')

payload_size = struct.calcsize("L") ### CHANGED

while True:

    # Retrieve message size
    packed_msg_size = sockfile.read(payload_size)
    
    msg_size = struct.unpack("L", packed_msg_size)[0] ### CHANGED

    # Retrieve all data based on message size
    
    frame_data = sockfile.read(msg_size)
   

    # Extract frame
    frame = pickle.loads(frame_data)

    # Display
    cv2.imshow('frame', frame)
    cv2.waitKey(1)