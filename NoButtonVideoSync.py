import os
import shutil


# New Video File Check State
NewVideoFile = False

# Setting dir path and file name
base_dir = "/home/pi/SyncPi8/"
usb_dir = "/media/usb0/"
local_video_file = 'SyncVideo.mp4'
usb_video_file = 'video2.mp4'

# getting local video size
try:
    videoinLocalSize = os.path.getsize(base_dir+local_video_file)
except:
    print 'No local video File'
    videoinLocalSize = 0

# getting usb video size
try:
    videoinUsbSize = os.path.getsize(usb_dir+usb_video_file)
except:
    print 'No Usb Video File'
    videoinUsbSize = 0

# display them
print "Video in Usb: ", videoinUsbSize
print "Video in Local: ", videoinLocalSize


def VideoFileState():
    global NewVideoFile
    if videoinLocalSize != videoinUsbSize and videoinLocalSize > 0 and videoinUsbSize > 0 :
        print "New Video found!"
        NewVideoFile = True
    if NewVideoFile:
        GPIO.output(RGB_BLUE, RGB_ENABLE)
    else:
        print "No New Video FIle Found"
        GPIO.output(RGB_GREEN, RGB_ENABLE)

def SyncFile():
    global NewVideoFile
    print 'Ready Sync File'
    if NewVideoFile:
        try:
            print 'Copying'
            GPIO.output(RGB_GREEN, RGB_ENABLE)
            shutil.copy(usb_dir+usb_video_file, base_dir+local_video_file)
            GPIO.output(RGB_GREEN, RGB_DISABLE)
            print 'Copy Success, Video Updated'
            NewVideoFile = False
            RGB_blink(RGB_BLUE)

            pass
        except:
            print 'Copy Error'
    else:
        'No New USB Video, Already Updated'
        RGB_blink(RGB_GREEN)

def main():
    global NewVideoFile
    VideoFileState()
    print NewVideoFile
    while NewVideoFile:
    SyncFile()




try:
    main()




finally:
    print("Closed Everything. END")


