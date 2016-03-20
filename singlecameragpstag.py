# Import modules to work with GPS unit and also the picamera
import gps
import picamera

# setup GPS

session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)


# see if we have a GPS fix
# if not then exit

while True:
	try:
		report = session.next()
		print report

	except StopInteration:
		session = None
		print "GPSD has terminated"
# get GPS location

# take image

# save image with GPS location in filename 
