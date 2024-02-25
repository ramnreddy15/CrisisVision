from typing import TypedDict
from gpiozero import DistanceSensor as gpiozero_DistanceSensor


class PinsConfig(TypedDict):
    echo: int
    trigger: int


class Config(TypedDict):
    pins: PinsConfig


class DistanceSensor(gpiozero_DistanceSensor):

    """child class of gpiozero.InputDevice, main functionality is instance property 'distance'"""

    def __init__(self, config: Config):
        super().__init__(config['pins']['echo'], config['pins']['trigger'])
