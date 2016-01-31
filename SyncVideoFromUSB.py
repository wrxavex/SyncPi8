import os
import shutil
# from gpiozero import LED, Button
# from signal import pause

base_dir = "/home/pi/SyncPi8/"
usb_dir = "/media/usb0/"

videoinLocalSize = os.path.getsize(base_dir+'synctest.mp4')
videoinUsbSize = os.path.getsize(usb_dir+'video0.m4v')
print "Video in Usb: ", videoinUsbSize
print "Video in Local: ", videoinLocalSize

# led = LED(17)
# button = Button(23)

def SyncFile():
    print 'Ready Sync File'
    try:
        print 'Copying'
        shutil.copy(usb_dir+'video0.m4v', base_dir+'video0.m4v')
        print 'Copy Success'
        pass
    except Error as err:
        print 'Error'

if videoinLocalSize != videoinUsbSize:



