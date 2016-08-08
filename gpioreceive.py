import picamera
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN)

while True:
	if GPIO.input(3):
		with picamera.PiCamera() as camera:
			camera.resolution = (2592,1944)
			camera.start_preview()
			time.sleep(2)
			camera.capture('test.jpg')
	else:
		time.sleep(0.1)

GPIO.cleanup()
