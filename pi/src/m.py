from typing import TypedDict
from gpiozero import PWMLED
from src.led import LED

class PinsConfig(TypedDict):
    speed: int
    control1: int
    control2: int


class Config(TypedDict):
    pins: PinsConfig


class Motor:

    pwm: PWMLED
    control1: LED
    control2: LED

    MAX_SPEED: float = 1.0

    def __init__(self, config: Config):

        self.pwm = PWMLED(config['pins']['speed'])
        self.control1 = LED({'pin': config['pins']['control1']})
        self.control2 = LED({'pin': config['pins']['control2']})

    def stop(self) -> None:
        """Stop the motor"""
        self._output(0.0, True, True)

    def forward(self, speed: float) -> None:
        """Spin the motor forward at a given speed"""
        self.drive(speed, True)

    def backward(self, speed: float) -> None:
        """Spin the motor backward at a given speed"""
        self.drive(speed, False)

    def drive(self, speed: float, direction: bool) -> None:
        """Spin the motor at a given speed and direction

        speed: float in [0, 1]
        direction: True for forward, False for backwards
        """

        self._output(speed, direction, not direction)

    def _output(self, speed: float, control1: bool, control2: bool) -> None:
        """Set the motor's speed, and send out the output signals"""

        # bound the speed to [MIN_SPEED, MAX_SPEED]
        speed = min(Motor.MAX_SPEED, max(0, speed))

        # set speed and output values
        self.pwm.value = speed
        self.control1.on() if control1 else self.control1.off()
        self.control2.on() if control2 else self.control2.off()
