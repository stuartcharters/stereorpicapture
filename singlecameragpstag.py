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
	
		report = session.next()
		if report['class']== 'TPV':
			print report
			if hasattr(report,'mode'):
				if report.mode !=1:
					# record location
					print "Has Fix"
					lat = report.lat
					long = report.lon
					t = time.time()
					# Take Image and store with filename using lat and long
					filename= "img" + str(lat) + "-" + str(long) + "-" + str(t) + ".jpg"
					with picamera.PiCamera() as camera:
						camera.resolution = (2592,1944)
						camera.start_preview()
						time.sleep(2)
						camera.capture(filename)
					

				else:
					print "No Fix"
				


# take image



# save image with GPS location in filename 
