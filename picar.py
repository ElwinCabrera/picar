"""
PI power
5V on pin
GND on pin

The GPIO mode is set to BCM


H-Bridge Motor Driver Pin Configuration
in1    -> BCM 05   (board pin 29 or GPIO 5)
in2    -> BCM 06   (board pin 31 or GPIO 6)
enable -> BCM 13   (board pin 33 or GPIO 13, PWM)

PCA9685 (16-Channel Servo Driver) Pin Configuration
SDA -> BCM 2 (board pin 3, GPIO 2)
SCL -> BCM 3 (board pin 5, GPIO 3)
VCC -> Board Pin 1 (3.3v)
GND -> Board Pin 9

HC-SR04 (Sonar Distance Sensor)
Trig -> BCM 23   (board pin 16 or GPIO 23)
Echo -> BCM 24   (board pin 18 or GPIO 24)
VCC -> Board Pin 17 (3.3v)
GND -> Board Pin 20
"""

from adafruit_servokit import ServoKit
from gpiozero import Motor, PWMOutputDevice
from time import sleep
from enum import Enum


class ServoCh(Enum):
    STEERING = 0
    CAM_PAN = 1
    CAM_TILT = 2

    TRIGHT_HYDR = 4
    TLEFT_HYDR = 5
    BRIGHT_HYDR = 6
    BLEFT_HYDR = 7


class PiCar:
    def __init__(self):
        self.motorDriver = HBridgeMotorDriver(in1=5, in2=6, enable=13)
        self.servoDiver = ServoDriver(sda=2, scl=3)

    def f(self):
        pass


class HBridgeMotorDriver:
    def __init__(self, in1, in2, enable):
        self.in1 = in1
        self.in2 = in2
        self.enable = enable  # this gpio is pwm
        self.pwmEnable = PWMOutputDevice(enable, frequency=100)
        self.motor = Motor(forward=in1, backward=in2)
        self.pwmEnable.on()
        self.currSpeed = 0.0

    # def start(self, startPWMDutyCycle: float = 1.0):
    #     self.pwmEnable.on()
    #     self.pwmEnable.value = startPWMDutyCycle
    #
    # def stop(self):
    #     self.pwmEnable.value = 0.0
    #     # self.pwmEnable.off()

    def slowStart(self, accelRate: int = 1, perSec: float = 1, speedFrom: float = 0):
        self.accelerate(rate=accelRate, perSec=perSec, speedFrom=speedFrom)
        self.pwmEnable.value = 0.0

    def slowStop(self, decelRate: int = 1, perSec: float = 1, speedFrom: float = 100):
        self.decelerate(rate=decelRate, perSec=perSec, speedFrom=speedFrom)
        self.pwmEnable.value = 0.0
        # self.pwmEnable.off()

    def accelerate(self, rate: int = 1, perSec: float = 1, speedFrom: float = 0, speedTo: float = 100):

        if speedFrom < 0 or speedTo < 0:
            # in physics its posible to have negative speed but lets keep it positive for now
            print("one of the speed is negative")
            return

        if speedTo > speedFrom:
            print("Cant accelerate to a speed less than the start speed, do you want to decelerate instead? ")
            print("ERROR: accelerate Speed From: {} -> Speed To: {}".format(speedFrom, speedTo))
            return

        if rate < 0:
            print("Cant accelerate at a negative rate, , do you want to decelerate instead?")
            return

        if rate == 0:
            print("going constant speed")
            return

        if rate > 100:
            rate = 100

        print("Accelerating at a rate of {} unit/sec".format(rate))
        for currRate in range(int(speedFrom), 101, rate):
            dutyCycle = currRate / 100
            self.pwmEnable.value = dutyCycle
            currSpeed = currRate / perSec
            print("Current Speed: {} unit/sec".format(currSpeed))
            if currSpeed >= speedTo:
                print("Accelerating stopped, speed limit of {} unit/sec reached".format(speedTo))
                break
            sleep(perSec)

    def decelerate(self, rate: int = 1, perSec: float = 1, speedFrom: float = 100, speedTo: float = 0):

        if speedFrom < 0 or speedTo < 0:
            # in physics its posible to have negative speed but lets keep it positive for now
            print("one of the speed is negative")
            return

        if speedTo > speedFrom:
            print("Cant decelerate to a speed higher than the start speed, do you want to accelerate instead? ")
            print("ERROR: Decelerate Speed From: {} -> Speed To: {}".format(speedFrom, speedTo))
            return

        if rate < 0:
            rate *= -1

        if rate == 0:
            print("going constant speed")
            return

        if rate > 100:
            rate = 100

        print("Decelerating at a rate of {} unit/sec".format(rate))
        for r in range(int(speedFrom), 101, rate):
            currRate = speedFrom - r
            dutyCycle = currRate / 100
            self.pwmEnable.value = dutyCycle

            currSpeed = currRate / perSec
            print("Current Speed: {} unit/sec".format(currSpeed))
            if currSpeed <= speedTo:
                print("Accelerating stopped, speed limit of {} unit/sec reached".format(speedTo))
                break
            sleep(perSec)

    def forward(self, pwmDutyCycle: float = 1.0):
        self.motor.forward()
        self.pwmEnable.value = pwmDutyCycle

    def backward(self, pwmDutyCycle: float = 1.0):
        # self.motor.backward(pwmDutyCycle)
        self.motor.backward()
        self.pwmEnable.value = pwmDutyCycle


    def halt(self):
        self.pwmEnable.off()


class ServoDriver:
    def __init__(self, sda, scl):
        self.sda = sda
        self.scl = scl
        # self.vccPin = 17
        # self.gndPin = 20
        self.kit = ServoKit(channels=16)


class DistanceSensor:
    pass


if __name__ == "__main__":
    try:
        print("")
    except KeyboardInterrupt:
        print("Program Stopped via keyboard interrupt")
