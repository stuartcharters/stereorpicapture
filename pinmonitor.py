import RPi.GPIO as GPIO
#GPIO.cleanup()
pin = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
while True:
    print GPIO.input(pin)
GPIO.cleanup()
