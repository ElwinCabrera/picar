from adafruit_servokit import ServoKit
#from gpiozero import Motor
#import RPi.GPIO as GPIO
import time

kit = ServoKit(channels=16)

WHEELS = 0
PAN = 1
TILT = 2

TOP_RIGHT_HYDR = 4
TOP_LEFT_HYDR = 5
BOTTOM_RIGHT_HYDR = 6
BOTTOM_LEFT_HYDR = 7

try:

	#kit.servo[PAN].angle = 0
	#kit.servo[TILT].angle = 0
	#kit.servo[TOP_RIGHT_HYDR].angle = 0
	#kit.servo[TOP_LEFT_HYDR].angle = 0
	#kit.servo[BOTTOM_RIGHT_HYDR].angle = 0
	#kit.servo[BOTTOM_LEFT_HYDR].angle = 0

	while True:
		servoNum = WHEELS
		for i in range(0,180,5):
			#print("Servo: ",servoNum,"Angle:",i)
	       		#kit.servo[servoNum].angle=i
			pwm.set_pwm(0, 1024,3072)
	        	time.sleep(0.05)

#		time.sleep(1)
except KeyboardInterrupt:
	print("Program Stopped via keyboard interrupt")
