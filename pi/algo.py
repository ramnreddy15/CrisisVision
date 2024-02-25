#Required Packages for Self-Driving Algorithm
import numpy
import threading
import time

#Image Processing and Networking Dependencies
import cv2
import numpy as np
import socket
import struct
from picamera2 import Picamera2

#DS Sensor and Motor Drivers
from src import ds
from src import m

#Distance Sensor Configurations
distance_sensor1 = ds.DistanceSensor({
    "pins": {
        "echo": 23,
        "trigger": 24
    }
})

distance_sensor2 = ds.DistanceSensor({
    "pins": {
        "echo": 17,
        "trigger": 27
    }
})

#Motor Configuration
motor1 = m.Motor({
    "pins": {
        "speed": 13,
        "control1": 5,
        "control2": 6
    }
})

motor2 = m.Motor({
    "pins": {
        "speed": 12,
        "control1": 7,
        "control2": 8
    }
})


class SDNode:
    def __init__(self):
        #Vehicle Clocking Variable
        self.clock = False
        #Vehicles Control Variables and Data
        self.ds1 = 0
        self.ds2 = 0
        self.speed = 2
        self.turnspeed = 1
        self.numPano = 5
        self.panaImages = [0 for i in range(self.numPano)]
        self.panacount = 0
        self.frame = np.zeros((480,640,3), dtype='uint8')
        
        #Start Sockets Connection to Send Real Time Image Data to Remote Monitors
        self.clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.clientsocket.connect(('192.168.111.51',8009))
        self.picam2 = Picamera2()
        self.config = self.picam2.create_preview_configuration({'format': 'RGB888'})
        self.picam2.configure(self.config)
        self.picam2.start()


    def getDSData(self):
        while True:
            if self.clock:
                self.ds1 = distance_sensor1.distance
                self.ds2 = distance_sensor2.distance
                time.sleep(0.1)
            else:
                break
    def selfDrive(self):
        global motor1,motor2
        while True:
            if self.clock:
                if(self.ds1 < 0.5 and self.ds2 < 0.5):
                    motor1.backward(self.speed)
                    motor2.backward(self.speed)
                    time.sleep(0.2)
                elif(self.ds1 > 0.5 and self.ds2 < 0.5):
                    motor2.backward(self.turnspeed)
                    motor1.forward(self.turnspeed)
                    time.sleep(0.2)
                    motor1.stop()
                    motor2.stop()
                    time.sleep(0.1)
                elif(self.ds1 < 0.5 and self.ds2 > 0.5):
                    motor1.backward(self.turnspeed)
                    motor2.forward(self.turnspeed)
                    time.sleep(0.2)
                    motor1.stop()
                    motor2.stop()
                    time.sleep(0.1)
                else:
                    motor1.forward(self.speed)
                    motor2.forward(self.speed)
                    time.sleep(0.2)
            else: 
                break
    def imgWrite(self):
        while True:
            self.frame = self.picam2.capture_array()


    def imgRelay(self):
        while True:
            if self.clock:    
                print(self.frame.size, self.frame.dtype)
                frameS = self.frame.tobytes()
                message_size = struct.pack(">Q", len(frameS))
                self.clientsocket.sendall(message_size)
                self.clientsocket.sendall(frameS)
            else: 
                break
    def panoramicDrive(self):
        while True:
            if not self.clock:    
                motor1.backward(self.turnspeed)
                motor2.forward(self.turnspeed)
                time.sleep(0.1)
                motor1.stop()
                motor2.stop()
                time.sleep(1)
            else: 
                break
    def panoramicMeshSend(self):
        while True:
            if not self.clock:
                if(self.panacount < self.numPano):
                    self.panaImages[self.panacount] = self.frame
                    self.panacount += 1
                    time.sleep(0.4)
                else:
                    stitcher = cv2.Stitcher_create()
                    status, result = stitcher.stitch(self.panaImages)
                    resultS = np.array(result)
                    print(resultS.shape)
                    size = str(resultS.shape).encode()
                    resultS = resultS.tobytes()
                    lR = len(resultS)
                    print(lR)
                    if(lR > 11):
                        message_size = struct.pack(">Q", len(size))
                        self.clientsocket.sendall(message_size)
                        self.clientsocket.sendall(size)
                        message_size = struct.pack(">Q", len(resultS))
                        self.clientsocket.sendall(message_size)
                        self.clientsocket.sendall(resultS)
                    self.panacount = 0
            else: 
                break

    def spawnThreads(self):
        threading.Thread(target=self.imgWrite).start()
        while True:
            self.clock = not self.clock
            threading.Thread(target=self.getDSData).start()
            threading.Thread(target=self.selfDrive).start()
            threading.Thread(target=self.imgRelay).start()
            time.sleep(45)
            self.clock = not self.clock
            threading.Thread(target=self.panoramicDrive).start()
            threading.Thread(target=self.panoramicMeshSend).start()
            time.sleep(15) 


def main():
    car = SDNode()
    car.spawnThreads()

if __name__ == "__main__":
    main()
