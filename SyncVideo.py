import RPi.GPIO as GPIO
import time
import os
import shutil


NewVideoFile = False

# Setting dir path and file name
base_dir = "/home/pi/SyncPi8/"
usb_dir = "/media/usb0/"
local_video_file = 'synctest.mp4'
usb_video_file = 'video4.mp4'

# getting local video size
videoinLocalSize = os.path.getsize(base_dir+local_video_file)

# getting usb video size
videoinUsbSize = os.path.getsize(usb_dir+usb_video_file)

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

def RGB_blink(speed):
    for val in RGB:
        GPIO.output(val, RGB_ENABLE)
        print val, "LED ON"
        time.sleep(speed)
        GPIO.output(val, RGB_DISABLE)
        print val, "LED OFF"


def VideoFileState():
    global NewVideoFile
    if videoinLocalSize != videoinUsbSize:
        print "New Video found!"
        NewVideoFile = True
    if NewVideoFile:
        GPIO.output(RGB_BLUE, RGB_ENABLE)

def SyncFile():
    global NewVideoFile
    print 'Ready Sync File'
    if NewVideoFile:
        try:
            print 'Copying'
            shutil.copy(usb_dir+local_video_file, base_dir+usb_video_file)
            print 'Copy Success'
            NewVideoFile = False
            GPIO.output(RGB_BLUE, RGB_DISABLE)
            pass
        except Error as err:
            print 'Error'



def main():
    led_setup()
    button_setup()
    button_init()
    VideoFileState()
    count1 = 0
    count2 = 0
    btn1_closed = True
    btn2_closed = True
    while True:
        btn1_state = GPIO.input(BTN1)
        if btn1_state != btn1_state_init and btn1_closed and btn2_closed:
            print "blink start"
            RGB_blink(1)
            print "blink over"
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





