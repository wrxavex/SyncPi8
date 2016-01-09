from gpiozero import LED, Button
from time import sleep
import os
import sys

DEBUG = True
SNDON = True
readyShutdwon = False

ledR = LED(22)
ledG = LED(27)
ledB = LED(17) 

ledB.on() # LED Bule is Lighting while App Running

button1 = Button(23, True, None)
button2 = Button(24, True, None)

button1StatePre = button1.is_pressed

def blinkR(count):
    global button1StatePre
    global readyShutdown
    readyShutdown = True
    while count > 0 :
        if button1StatePre != button1.is_pressed : 
            button1StatePre = button1.is_pressed
            readyShutdown = False
            break
        ledR.on()
        sleep(0.5)
        ledR.off()
        sleep(0.5)
        count -= 1


def doShutdown():
    global button1StatePre
    global ledB
    global readyShutdown 

    button1StatePre = button1.is_pressed
    print ("Countdown for Shutdown in 3sec")
    blinkR(3)
    if readyShutdown:
        print ("Countdown Over Shutdown now")
        ledB.off()
        sys.exit()




def main():
    while True:
        global button1StatePre
        print ('button1StatePre: ', button1StatePre)
        if button1.is_pressed != button1StatePre : doShutdown()
        button2.when_pressed = ledG.on
        button2.when_released = ledG.off
        sleep(1)
        print ('button1:',button1.is_pressed, 'button2:', button2.is_pressed)


try:
    main()

finally:
    print("Closed Everything. END")
    ledB.off() # LED Blue is off when App is down

#End
