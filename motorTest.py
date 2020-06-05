#from gpiozero import Motor
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
input1 = 29
input2 = 31
enable = 33

GPIO.setup(input1, GPIO.OUT)
GPIO.setup(input2, GPIO.OUT)
GPIO.setup(enable, GPIO.OUT)

en = GPIO.PWM(enable, 5000)
MIN_START_DUTY = 35


try:
	en.start(100)
	time.sleep(0.5)

	while True:
		#GPIO.output(enable, GPIO.HIGH)

		#GPIO.output(input1, GPIO.HIGH)
		#GPIO.output(input2, GPIO.LOW)
		#time.sleep(3)
		GPIO.output(input1, GPIO.LOW)
		GPIO.output(input2, GPIO.HIGH)
		#time.sleep(3)

		#for duty in range(MIN_START_DUTY,101, 5):
		#	print("Changing duty Cycle to:",duty)
		#	en.ChangeDutyCycle(duty)
		#	time.sleep(1)

		for duty in range (100, MIN_START_DUTY-1, -5):
			print("Changing duty Cycle to:",duty)
			en.ChangeDutyCycle(duty)
			time.sleep(3)
		print("stopping for 3 seconds")
		#en.stop()
		#en.ChangeDutyCycle(MIN_START_DUTY)
		time.sleep(1)
except KeyboardInterrupt:
	print("Program Stopped via keyboard interrupt")
	en.stop()
	GPIO.output(enable, GPIO.LOW)
	GPIO.cleanup()
