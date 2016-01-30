mport RPi.GPIO as GPIO
import time

# SyncPi Hardware Test
# P1
# 2[ == FV FN == == == GN B1 B2 GN == ...]
# 1[ == == == == GN RH GH BH .. .. .. ...]

RGB_ENABLE = 1; RGB_DISABLE = 0

# LED CONFIG Set GPIO Ports

RGB_RED = 17; RGB_GREEN = 27; RGB_BLUE = 22
RGB = [RGB_RED, RGB_GREEN, RGB_BLUE]

def led_setup():
    GPIO.setmode(GPIO.BCM)
    for val in RGB:
        GPIO.setup(val, GPIO.OUT)

def main():
    led_setup()
    for val in RGB:
        GPIO.output(val, RGB_ENABLE)
        print val, "LED ON"
        time.sleep(1)
        GPIO.output(val, RGB_DISABLE)
        print val, "LED OFF"
        
try:
    main()

finally:
    GPIO.cleanup()
    print("Closed Everything. END")
