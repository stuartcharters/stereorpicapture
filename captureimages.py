import sys
import time
import picamera
import RPi.GPIO as GPIO
savelocation= ""
# function to take picture
def takepic():
    t = time.time()
    with picamera.PiCamera() as camera:
        camera.resolution = (2592,1944)
        camera.start_preview()
        time.sleep(2)
        camera.capture(savelocation + str(t) + '.jpg')

# main function of program
def main(argv):
    role = argv[0]
    pin = int(argv[3])
    GPIO.setmode(GPIO.BOARD)
    if role == "master":
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
        while True:
            GPIO.output(pin, GPIO.HIGH)
            takepic()
            GPIO.output(pin, GPIO.LOW)

    else:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(pin, GPIO.RISING)
        GPIO.add_event_callback(pin,takepic,100)
        while True:
            GPIO.wait_for_edge(pin)
    GPIO.cleanup()


if __name__=="__main__":
    savelocation = "/mnt/" + str(sys.argv[3])  + "-" + str(sys.argv[2]) + "-"
    main(sys.argv[1:])
