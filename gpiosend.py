import time
import picamera
import RPi.GPIO as GPIO
pin = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT, initial= GPIO.LOW)

while True:
	GPIO.output(pin, GPIO.HIGH)
	t = time.time()
	with picamera.PiCamera() as camera:
		camera.resolution = (2592,1944)
		camera.start_preview()
		GPIO.output(pin, GPIO.LOW)
		time.sleep(2)
		camera.capture(str(t)+'.jpg')

GPIO.cleanup()
