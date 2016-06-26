#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import os
import time
import platform
from time import sleep
import RPi.GPIO as GPIO


hostname = platform.node()
os.environ['TZ'] = 'Asia/Taipei'
time.tzset()

font_file = "/home/pi/SyncPi8/msjh.ttc"
os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()
pygame.mouse.set_visible(False)
lcd = pygame.display.set_mode((320, 240))
lcd.fill((0, 0, 0))
pygame.display.update()
