import time
import picamera
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN)

while True:
	GPIO.wait_for_edge(3,GPIO.RISING)
	with picamera.PiCamera() as camera:
		camera.resolution = (2592,1944)
		camera.start_preview()
		time.sleep(2)
		camera.capture('test.jpg')

GPIO.cleanup()
