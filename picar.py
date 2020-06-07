"""
PI power
5V on pin
GND on pin

The GPIO mode is set to BCM


H-Bridge Motor Driver Pin Configuration
in1    -> BCM 12   (board pin 32 or GPIO 12, PWM)
in2    -> BCM 13   (board pin 33 or GPIO 13, PWM)
enable -> Not Used

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
from time import sleep


class PiCar:
    def __init__(self):
        self.servoDiver = ServoDriver(sda=2, scl=3)



class ServoDriver:
    def __init__(self, sda, scl):
        self.sda = sda
        self.scl = scl
        # self.vccPin = 17
        # self.gndPin = 20
        self.kit = ServoKit(channels=16)

    def moveStearing(self, deg: int):
        self.kit.servo[2].angle = deg

    def moveCameraPan(self, deg: int):
        pass

    def moveCameratilt(self, deg: int):
        pass

    def moveHydroTL(self, deg: int):
        pass

    def moveHydroTR(self, deg: int):
        pass

    def moveHydroBL(self, deg: int):
        pass

    def moveHydroBR(self, deg: int):
        pass

    def testing(self):
        pass


if __name__ == "__main__":
    car = PiCar()
    try:
        while 1:
            #car.motorDriver.testing(1.0)
            for d in range(0, 181, 5):
                car.servoDiver.moveStearing(d)

    except KeyboardInterrupt:
        print("Program Stopped via keyboard interrupt")
        #car.motorDriver.halt()
