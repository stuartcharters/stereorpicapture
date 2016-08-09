import time
import picamera
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT, initial= GPIO.LOW)

while True:
	GPIO.output(7, GPIO.HIGH)
	t = time.time()
	with picamera.PiCamera() as camera:
		camera.resolution = (2592,1944)
		camera.start_preview()
		GPIO.output(7, GPIO.LOW)
		time.sleep(2)
		camera.capture(t+'.jpg')

GPIO.cleanup()
