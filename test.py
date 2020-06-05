from adafruit_servokit import ServoKit
#from gpiozero import Motor
import RPi.GPIO as GPIO
import time

#GPIO.setmode(GPIO.BOARD)
input1 = 29
input2 = 31
enable = 33

#GPIO.setup(input1, GPIO.OUT)
#GPIO.setup(input2, GPIO.OUT)
#GPIO.setup(enable, GPIO.OUT)

#en = GPIO.PWM(enable, 5000)
MIN_START_DUTY = 35
#motor = Motor(forward=11, backward=13)
kit = ServoKit(channels=16)

WHEELS = 0
PAN = 1
TILT = 2

TOP_RIGHT_HYDR = 4
TOP_LEFT_HYDR = 5
BOTTOM_RIGHT_HYDR = 6
BOTTOM_LEFT_HYDR = 7

try:
#	en.start(100)
#	time.sleep(0.5)

	#kit.servo[PAN].angle = 0
	#kit.servo[TILT].angle = 0
	#kit.servo[TOP_RIGHT_HYDR].angle = 0
	#kit.servo[TOP_LEFT_HYDR].angle = 0
	#kit.servo[BOTTOM_RIGHT_HYDR].angle = 0
	#kit.servo[BOTTOM_LEFT_HYDR].angle = 0

	while True:
		servoNum = PAN
		for i in range(0,180,5):
			#print("Servo: ",servoNum,"Angle:",i)
	       		kit.servo[servoNum].angle=i
	        	time.sleep(0.05)

		#GPIO.output(enable, GPIO.HIGH)

		#GPIO.output(input1, GPIO.HIGH)
		#GPIO.output(input2, GPIO.LOW)
		#time.sleep(3)
#		GPIO.output(input1, GPIO.LOW)
#		GPIO.output(input2, GPIO.HIGH)
		#time.sleep(3)

		#for duty in range(MIN_START_DUTY,101, 5):
		#	print("Changing duty Cycle to:",duty)
		#	en.ChangeDutyCycle(duty)
		#	time.sleep(1)

#		for duty in range (100, MIN_START_DUTY-1, -5):
#			print("Changing duty Cycle to:",duty)
#			en.ChangeDutyCycle(duty)
#			time.sleep(2)
#		print("stopping for 3 seconds")
		#en.stop()
		#en.ChangeDutyCycle(MIN_START_DUTY)
#		time.sleep(1)
except KeyboardInterrupt:
	print("Program Stopped via keyboard interrupt")
	en.stop()
	GPIO.output(enable, GPIO.LOW)
	GPIO.cleanup()
