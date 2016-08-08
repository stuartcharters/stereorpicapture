import time
import picamera
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT, initial= GPIO.LOW)

while True:
	GPIO.output(3, GPIO.HIGH)
	with picamera.PiCamera() as camera:
		camera.resolution = (2592,1944)
		camera.start_preview()
		GPIO.OUTPUT(3, GPIO.LOW)
		time.sleep(2)
		camera.capture('test.jpg')

GPIO.cleanup()
