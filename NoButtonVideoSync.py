import os
import shutil
import time


# record time
os.environ['TZ'] = 'Asia/Taipei'
print time.strftime('%X %x %Z')


# New Video File Check State
NewVideoFile = False

# Setting dir path and file name
base_dir = "/home/pi/SyncPi8/"
usb_dir = "/media/usb0/"
local_video_file = 'SyncVideo.mp4'
usb_video_file = 'video1.mp4'



def VideoFileState(usb_video_file):
    global NewVideoFile
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

    if videoinLocalSize != videoinUsbSize and videoinLocalSize > 0 and videoinUsbSize > 0 :
        NewVideoFile = True
    if NewVideoFile:
        print "New Video found!"
    else:
        print "No New Video FIle Found"


def SyncFile(usb_video_file):
    global NewVideoFile
    global time_now
    print 'Ready Sync File'
    if NewVideoFile:
        try:
            print 'Copying'
            shutil.copy(usb_dir+usb_video_file, base_dir+local_video_file)
            print 'Copy Success, Video Updated'
            NewVideoFile = False

            pass
        except:
            print 'Copy Error'
    else:
        print ('No New USB Video')
        return 'No New USB Video, Already Updated'


def main(usb_video_file):
    global NewVideoFile
    VideoFileState(usb_video_file)
    # print NewVideoFile
    while NewVideoFile:
        SyncFile(usb_video_file)


if __name__ == '__main__':
    try:
        main(usb_video_file)

    finally:
        print("Closed Everything. END")
        print "\n"
