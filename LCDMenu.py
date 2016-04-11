#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import os
import time
import platform
from time import sleep
import subprocess
import thread





# Set timezone

hostname = platform.node()
os.environ['TZ'] = 'Asia/Taipei'
time.tzset()

font_file = "/home/pi/SyncPi8/msjh.ttc"


# Colours
WHITE = (255, 255, 255)

# os.putenv('SDL_FBDEV', '/dev/fb1') # Target Display

pygame.init()
pygame.mouse.set_visible(False)
lcd = pygame.display.set_mode((800, 480))
lcd.fill((0, 0, 0))
pygame.display.update()

font_big = pygame.font.Font(font_file, 60)
font_small = pygame.font.Font(font_file, 180)
font_date = pygame.font.Font(font_file, 60)
font_time = pygame.font.Font(font_file, 180)
font_hostname = pygame.font.Font(font_file, 60)
font_myip = pygame.font.Font(font_file, 60)
font_setting = pygame.font.Font(font_file,60)
font_have_new_video = pygame.font.Font(font_file,60)





def main():
    while True:
        # Scan the buttons
        sleep(1)
        time_now = time.strftime('%X')
        date_now = time.strftime('%x %w')
        tft_update(time_now, date_now)


def tft_update(time_now, date_now):
    global count
    lcd.fill((0, 0, 0))
    text_surface_time = font_time.render(u'%s' % time_now, True, WHITE)
    text_surface_date = font_date.render(u'%s' % date_now, True, WHITE)
    #env_text = subprocess.check_output(["/home/pi/Adafruit_Python_DHT/examples/AdafruitDHT.py", "22", "23"])
    #text_surface_env_text = font_small.render('%s' % env_text, True, WHITE)

    rect_time = text_surface_time.get_rect(center=(400, 200))
    rect_date = text_surface_date.get_rect(center=(400, 320))
    #rect_env_text = text_surface_env_text.get_rect(center=(400,400))

    lcd.blit(text_surface_time, rect_time)
    lcd.blit(text_surface_date, rect_date)
    #lcd.blit(text_surface_env_text, rect_env_text)

    pygame.display.update()


if __name__ == '__main__':
    print ("Display info")
    main()
