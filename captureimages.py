import sys
import time
import picamera
import RPi.GPIO as GPIO
savelocation= ""
#variable used for a count of the number of photos taken
piccount = 0
#variable for the time to sleep after taking a photo in seconds
sleepaftertaking = 2
#variable to set the number of photos to take - count from zero
photostotake = 65;

# function to take picture
def takepic(channel=0):
    #t = time.time()
    #t = count
    global piccount
    global savelocation
    count = piccount
    piccount = piccount + 1
    with picamera.PiCamera() as camera:
        camera.resolution = (2592,1944)
        camera.start_preview()
        time.sleep(1)
        camera.capture(savelocation + str(time.strftime("%Y%m%d_%H%M%S")) + str(count) + '.jpg')
        time.sleep(sleepaftertaking)
        
# main function of program
def main(argv):
    role = argv[0]
    pin = int(argv[3])
    GPIO.setmode(GPIO.BOARD)
    if role == "master":
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
        while (piccount <= photostotake):
            GPIO.output(pin, GPIO.HIGH)
            takepic()
            GPIO.output(pin, GPIO.LOW)
            time.sleep(5)


    else:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(pin, GPIO.RISING)
        GPIO.add_event_callback(pin,takepic)
        while (piccount <= (photostotake-1)):
            time.sleep(0.01)
    GPIO.cleanup()


if __name__=="__main__":
    savelocation = "/mnt/" + str(sys.argv[3])  + "-" + str(sys.argv[2]) + "-"
    piccount = 0
    main(sys.argv[1:])
