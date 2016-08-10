import RPi.GPIO as GPIO
#GPIO.cleanup()
print GPIO.VERSION
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.cleanup()
