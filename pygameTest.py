#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import os
from time import sleep
import RPi.GPIO as GPIO

count = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
button_pre = 10 
#Note #21 changed to #27 for rev2 Pi
button_map = {23:(255,0,0), 22:(0,255,0), 24:(0,0,255), 5:(0,0,0)}
 
#Setup the GPIOs as inputs with Pull Ups since the buttons are connected to GND
GPIO.setmode(GPIO.BCM)
for k in button_map.keys():
    GPIO.setup(k, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 
#Colours
WHITE = (255,255,255)
 
os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()
pygame.mouse.set_visible(False)
lcd = pygame.display.set_mode((320, 240))
lcd.fill((0,0,0))
pygame.display.update()
 
font_big = pygame.font.Font("msjh.ttc", 72)
font_small = pygame.font.Font("msjh.ttc", 36)
def button_check(k):
    global button_pre
    global count1
    global count2
    global count3
    global count4
    if k == 23 and button_pre != 23:
        count1 = count1 + 1
        return count1
    if k == 22 and button_pre != 22:
        count2 = count2 + 1
        return count2
    if k == 24 and button_pre != 24:
        count3 = count3 + 1
        return count3
    if k ==  5 and button_pre != 5:
        count4 = count4 + 1
        return count4
    else:
        return count

        

while True:
    # Scan the buttons
    for (k,v) in button_map.items():
        if GPIO.input(k) == False:
            count = button_check(k)
            print count
            lcd.fill(v)
            text_surface = font_big.render(u'按鈕 %d'%k, True, WHITE)
            rect = text_surface.get_rect(center=(160,120))
            lcd.blit(text_surface, rect)
            text_surface = font_small.render(u'%d計數'%count, True, WHITE)
            rect = text_surface.get_rect(center=(240,200))
            lcd.blit(text_surface, rect)
            if button_pre !=k:
                pygame.display.update()
            button_pre = k 

    sleep(0.1)

    

