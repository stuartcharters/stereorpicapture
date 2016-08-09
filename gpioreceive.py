import time
import picamera
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
	print "Before wait"
	print GPIO.input(3)
	GPIO.wait_for_edge(3,GPIO.RISING)
	with picamera.PiCamera() as camera:
		camera.resolution = (2592,1944)
		#camera.start_preview()
		print "after wait"
		print GPIO.input(3)
		time.sleep(2)
		#camera.capture('test.jpg')

GPIO.cleanup()
