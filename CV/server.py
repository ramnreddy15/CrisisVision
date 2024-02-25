import json
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
        # doing it in batches is generally better than trying
        # to do it all in one go, so I believe.
        to_read = length - len(data)
        data += conn.recv(
            4096 if to_read > 4096 else to_read)

    # send our 0 ack
    data = json.loads(data.decode())
    data = np.array(data).astype(np.uint8)
    # cv2.imwrite("test.jpg", data)
    cv2.imshow('frame', data)
    cv2.waitKey(1)

# sockfile = conn.makefile('rb')

# payload_size = struct.calcsize("L") ### CHANGED

# while True:

#     # Retrieve message size
#     packed_msg_size = sockfile.read(payload_size)

#     msg_size = struct.unpack("L", packed_msg_size)[0] ### CHANGED

#     # Retrieve all data based on message size

#     frame_data = sockfile.read(msg_size)


#     # Extract frame
#     frame = json.loads(frame_data)

#     # Display
#     cv2.imshow('frame', frame)
#     cv2.waitKey(1)