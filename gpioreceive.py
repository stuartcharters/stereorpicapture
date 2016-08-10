import time
import picamera
import RPi.GPIO as GPIO
#GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
time.sleep(1)
GPIO.add_event_detect(7, GPIO.BOTH)
while True:
	if GPIO.event_detected(7):
		signalRising = GPIO.input(7)
		if signalRising:
			t = time.time()
			with picamera.PiCamera() as camera:
				camera.resolution = (2592,1944)
				camera.start_preview()
				time.sleep(2)
				camera.capture(str(t) + '.jpg')
	else:
			sleep(0.01)

GPIO.cleanup()
