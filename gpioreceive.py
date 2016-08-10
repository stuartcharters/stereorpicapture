import time
import picamera
import RPi.GPIO as GPIO
#GPIO.cleanup()
pin = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
time.sleep(1)
GPIO.add_event_detect(pin, GPIO.BOTH)
while True:
	if GPIO.event_detected(pin):
		signalRising = GPIO.input(pin)
		if signalRising:
			t = time.time()
			with picamera.PiCamera() as camera:
				camera.resolution = (2592,1944)
				camera.start_preview()
				time.sleep(2)
				camera.capture(str(t) + '.jpg')
	else:
			time.sleep(0.01)

GPIO.cleanup()
