import time
import picamera
import RPi.GPIO as GPIO

# function to take picture
def takepic():
    t = time.time()
    with picamera.PiCamera() as camera:
        camera.resolution = (2592,1944)
        camera.start_preview()
        time.sleep(2)
        camera.capture(str(t) + '.jpg')

# main function of program
def main():
    pin = 7
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(pin, GPIO.RISING)
    GPIO.add_event_callback(pin,takepic,100)
    while True:
        GPIO.wait_for_edge(pin)
    GPIO.cleanup()


if __name__=="__main__":
    main()
