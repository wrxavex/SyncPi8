import os
videoinLocalSize = os.path.getsize('/home/pi/SyncPi8/synctest.mp4')
videoinUsbSize = os.path.getsize('/media/usb0/IMG_3182.m4v')
print "Video in Usb: ", videoinUsbSize
print "Video in Local: ", videoinLocalSize
