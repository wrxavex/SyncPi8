import RPi.GPIO as GPIO
import time
import os
import sys
import shutil

# Ready Shutdown State
readyShutdown = False


# New Video File Check State
NewVideoFile = False

# Setting dir path and file name
base_dir = "/home/pi/SyncPi8/"
usb_dir = "/media/usb0/"
local_video_file = 'synctest.mp4'
usb_video_file = 'video4.mp4'

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


# SyncPi Hardware Test
# P1
# 2[ == FV FN == == == GN B1 B2 GN == ...]
# 1[ == == == == GN RH GH BH .. .. .. ...]

RGB_ENABLE = 1; RGB_DISABLE = 0

# LED CONFIG Set GPIO Ports

GPIO.setmode(GPIO.BCM)

RGB_RED = 17; RGB_GREEN = 27; RGB_BLUE = 22
RGB = [RGB_RED, RGB_GREEN, RGB_BLUE]

BTN1 = 23; BTN2 = 24
BUTTON = [BTN1, BTN2]
btn1_state_init = False
btn2_state_init = False

def button_init():
    global btn1_state_init
    global btn2_state_init
    btn1_state_init = GPIO.input(BTN1)
    btn2_state_init = GPIO.input(BTN2)

def led_setup():
    for val1 in RGB:
        GPIO.setup(val1, GPIO.OUT)

def button_setup():
    for val2 in BUTTON:
        GPIO.setup(val2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def RGB_blink(val):
    for color in RGB:
        GPIO.output(color, RGB_DISABLE)
    for i in range(0,3, 1):
        GPIO.output(val, RGB_ENABLE)
        print val, "LED ON"
        time.sleep(0.3)
        GPIO.output(val, RGB_DISABLE)
        print val, "LED OFF"
        time.sleep(0.3)


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
            shutil.copy(usb_dir+local_video_file, base_dir+usb_video_file)
            print 'Copy Success, Video Updated'
            NewVideoFile = False
            RGB_blink(RGB_BLUE)

            pass
        except Error as err:
            print 'Error'
    else:
        'No New USB Video, Already Updated'
        RGB_blink(RGB_GREEN)


def doShutdown():
    global readyShutdown


    print ("Countdown for Shutdown in 3sec")
    if readyShutdown:
        print ("Countdown Over Shutdown now")
        os.system("flite -t 'System Shutdown down'")
        os.system("sudo shutdown -h now")
        sys.exit()



def main():
    led_setup()
    button_setup()
    button_init()
    VideoFileState()
    global readyShutdown
    count1 = 0
    count2 = 0
    btn1_closed = True
    btn2_closed = True
    while True:
        btn1_state = GPIO.input(BTN1)
        if btn1_state != btn1_state_init and btn1_closed and btn2_closed:
            print "Run Shutdown Script"
            RGB_blink(RGB_RED)
            readyShutdown = True
            doShutdown()
            print "When Run this is bug "
            btn1_closed = False
        elif btn1_state == btn1_state_init and btn1_closed == False:
            count1+=1
            print "CLOSE Button 1 %s times" % count1
            btn1_closed = True

        btn2_state = GPIO.input(BTN2)
        if btn2_state != btn2_state_init and btn2_closed and btn1_closed:
            print "Call USB Video Sync Script"
            SyncFile()
            print "USB Video Sync Script Done !"
            btn2_closed = False
        elif btn2_state == btn2_state_init and btn2_closed == False:
            count2+=1
            print "CLOSE Button 2 %s times" % count2
            btn2_closed = True

        time.sleep(0.1)


try:
    main()

finally:
    GPIO.cleanup()
    print("Closed Everything. END")





