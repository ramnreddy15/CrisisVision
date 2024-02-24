import cv2
import socket
import struct
import pickle

class VideoCamera(object):
    def __init__(self):
        self.clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientsocket.connect(('192.168.252.241',5000)) # Replace with your server IP and port
        self.data = b''
        self.payload_size = struct.calcsize("L")

    def __del__(self):
        self.clientsocket.close()

    def get_frame(self):
        while len(self.data) < self.payload_size:
            self.data += self.clientsocket.recv(4096)

        packed_msg_size = self.data[:self.payload_size]
        self.data = self.data[self.payload_size:]
        msg_size = struct.unpack("L", packed_msg_size)[0]

        while len(self.data) < msg_size:
            self.data += self.clientsocket.recv(4096)

        frame_data = self.data[:msg_size]
        self.data = self.data[msg_size:]

        frame = pickle.loads(frame_data)
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()