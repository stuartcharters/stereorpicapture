import RPi.GPIO as GPIO
#GPIO.cleanup()
pin = 11
GPIO.setmode(GPIO.BOARD)
print GPIO.input(pin)
GPIO.cleanup()
