# Import modules to work with GPS unit and also the picamera
import gps
import picamera
import time

# setup GPS

session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

lat = 0;
long = 0;

# see if we have a GPS fix
# if not then exit
# if we do (mode 2/3) then record the location for the image

while True:
	try:
		report = session.next()
		if report['class']== 'TPV':
			if hasattr(report,'mode'):
				if report.mode !=1:
					# record location
					print "Has Fix"
					lat = report.lat
					long = report.long
					# Take Image and store with filename using lat and long
					filename= "img" + lat + "-" + long + ".jpg"
					with picamera.PiCamera() as camera:
						camera.resolurion(1024,768)
						camera.start_preview()
						time.sleep(2)
						camera.capture(filename)
					

				else:
					print "No Fix"
				

	except StopInteration:
		session = None
		print "GPSD has terminated"



# take image



# save image with GPS location in filename 
