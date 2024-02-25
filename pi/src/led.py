import RPi.GPIO as GPIO
from typing import TypedDict


class Config(TypedDict):
    pin: int


class LED:

    pin: int

    def __init__(self, config: Config):
        self.pin = config['pin']
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def off(self):
        GPIO.output(self.pin, GPIO.LOW)
