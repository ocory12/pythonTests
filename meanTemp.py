import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)

counter = 0
totalTemp = 0
meanTemp = 0

while True:
	counter = counter+1 
	inputTemp = input("Input Current temp : ")
	print "Current Temp is", + inputTemp
	totalTemp = totalTemp+inputTemp
	meanTemp = totalTemp/counter
	print "Current Average is:", + meanTemp 
	GPIO.output(18,GPIO.LOW)
	GPIO.output(16,GPIO.LOW)
	if inputTemp < 24:
		print "Warning Temp is too low"
		GPIO.output(18,GPIO.HIGH)
		GPIO.output(16,GPIO.LOW)
	if inputTemp > 27:
		print "Warning Temp is too high"
		GPIO.output(16,GPIO.HIGH)
		GPIO.output(18,GPIO.LOW)
	time.sleep(1)
