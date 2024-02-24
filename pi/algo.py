#Required Packages for Self-Driving Algorithm
import asyncio
import numpy
import threading
import time

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
        self.ds1 = 0
        self.ds2 = 0
        self.speed = 5

    def getDSData(self):
        while True:
            self.ds1 = distance_sensor1.distance
            self.ds2 = distance_sensor2.distance


    def selfDrive(self):
        while True:
            if(self.ds1 < 0.1 and self.ds2 < 0.1):
                print("object avoidance")
                motor1.backward(self.speed)
                motor2.forward(self.speed)
                time.sleep(1)
            elif(self.ds1 > 0.1 and self.ds2 < 0.1):
                print("turn left")
                motor1.backward(self.speed)
                motor2.forward(self.speed)
                time.sleep(0.1)
            elif(self.ds1 < 0.1 and self.ds2 > 0.1):
                print("turn right")
                motor2.backward(self.speed)
                motor1.forward(self.speed)
                time.sleep(0.1)
            else:
                print("exploring")
                motor1.forward(self.speed)
                motor2.forward(self.speed)
                time.sleep(0.1)

    def spawnThreads(self):
        threading.Thread(target=self.getDSData).start()
        threading.Thread(target=self.selfDrive).start()


def main():
    car = SDNode()
    car.spawnThreads()

if __name__ == "__main__":
    main()
