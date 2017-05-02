import time 
import os 
import errno
from picamera import PiCamera

day = 1
RecordTime = 1440*day
interval = 3
getthedate = "20170501"

camera = PiCamera()
camera.resolution = (3280,2464)

for i in range(RecordTime):
    getcurrentdate = time.strftime("%Y%m%d")
    if getthedate != getcurrentdate:
        getthedate = getcurrentdate
        mydir = "/home/pi/Desktop/"+getthedate
        try:
            os.makedirs(mydir)
        except OSError:
            if not os.path.isdir(mydir):
                raise
        os.chdir(mydir)
    filename = 'img'+time.strftime("%H:%M")+'.jpg'
    camera.capture(filename)
    time.sleep(interval)

#runstill = ("raspistill -w 1280 -h 720 -tl 10 -t 50 -o "+mydir+"/pic%03d.jpg")
#os.system(runstill)
