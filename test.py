"""
PI power
5V on pin
GND on pin

The GPIO mode is set to BCM


H-Bridge Motor Driver Pin Configuration
in1    -> BCM --   (board pin 29 or GPIO )
in2    -> BCM --   (board pin 31 or GPIO )
enable -> BCM --   (board pin 33 or GPIO )

PCA9685 (16-Channel Servo Driver) Pin Configuration
SCL
SDA
VCC
GND

HC-SR04 (Sonar Distance Sensor)
Trig
Echo
VCC
GND


"""

from adafruit_servokit import ServoKit
from gpiozero import Motor, CompositeDevice
from time import sleep
from enum import Enum

kit = ServoKit(channels=16)


class Ch(Enum):
    STEERING = 0
    CAM_PAN = 1
    CAM_TILT = 2

    TRIGHT_HYDR = 4
    TLEFT_HYDR = 5
    BRIGHT_HYDR = 6
    BLEFT_HYDR = 7


class HBridgeMotorDriver:
    def __init__(self):
        self.in1 = 29
        self.in2 = 31
        self.enable = 33


class Servos:
    def __init__(self):
        self.scl = 0
        self.sda = 0
        self.vcc = 0
        self.gnd = 0


class DistanceSensor:
    pass


if __name__ == "__main__":
    try:
        print("")
    except KeyboardInterrupt:
        print("Program Stopped via keyboard interrupt")
