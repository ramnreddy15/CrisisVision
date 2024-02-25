#Required Packages for Self-Driving Algorithm
import asyncio
import numpy
import threading
import time

#Image Processing and Networking Dependencies
import cv2
import numpy as np
import socket
import struct
from picamera2 import Picamera2

#Object Detection and Annotation
import supervision as sv
from ultralytics import YOLO

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

#You Only Look Once (YOLO)
box_annotator = sv.BoxAnnotator(
    thickness=2,
    text_thickness=2,
    text_scale=1
)
label_annotator = sv.LabelAnnotator()


class SDNode:
    def __init__(self):
        #Vehicles Object Detection Model
        self.model = YOLO("yolov8n.pt")
        #Vehicles Control Variables and Data
        self.ds1 = 0
        self.ds2 = 0
        self.speed = 5
        self.turnspeed = 2
        #Start Sockets Connection to Send Real Time Image Data to Remote Monitors
        self.clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.clientsocket.connect(('192.168.111.51',8009))
        self.picam2 = Picamera2()
        self.config = self.picam2.create_preview_configuration({'format': 'RGB888'})
        self.picam2.configure(self.config)
        self.picam2.start()

    def getDSData(self):
        while True:
            self.ds1 = distance_sensor1.distance
            self.ds2 = distance_sensor2.distance
            time.sleep(0.1)

    def selfDrive(self):
        global motor1,motor2
        while True:
            if(self.ds1 < 0.5 and self.ds2 < 0.5):
                motor1.backward(self.speed)
                motor2.backward(self.speed)
            elif(self.ds1 > 0.5 and self.ds2 < 0.5):
                motor2.backward(self.turnspeed)
                motor1.forward(self.turnspeed)
                time.sleep(0.1)
                motor1.stop()
                motor2.stop()
                time.sleep(0.1)
            elif(self.ds1 < 0.5 and self.ds2 > 0.5):
                motor1.backward(self.turnspeed)
                motor2.forward(self.turnspeed)
                time.sleep(0.1)
                motor1.stop()
                motor2.stop()
                time.sleep(0.1)
            else:
                motor1.forward(self.speed)
                motor2.forward(self.speed)

    def imgProc(self):
        while True:
            frame = self.picam2.capture_array()
            result = self.model(frame, conf=0.2)[0]
            detections = sv.Detections.from_ultralytics(result)

            labels = [
                self.model.model.names[class_id]
                for class_id
                in detections.class_id
            ]

            frame = box_annotator.annotate(
                scene=frame,
                detections=detections,
                labels=labels
                )
            
            frameS = frame.tobytes()
            message_size = struct.pack(">Q", len(frameS))
            self.clientsocket.sendall(message_size)
            self.clientsocket.sendall(frameS)
           
    def spawnThreads(self):
        threading.Thread(target=self.getDSData).start()
        threading.Thread(target=self.selfDrive).start()
        threading.Thread(target=self.imgProc).start()


def main():
    car = SDNode()
    car.spawnThreads()

if __name__ == "__main__":
    main()
