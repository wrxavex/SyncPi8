#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import os
import time
import platform
from time import sleep
import subprocess
import thread


env_text = "Sensor Data Loading"
env_get_time = ""
env_count = 0
time_count = 0

# Set timezone

hostname = platform.node()
os.environ['TZ'] = 'Asia/Taipei'
time.tzset()

font_file = "/home/pi/SyncPi8/msjh.ttc"


# Colours
WHITE = (255, 255, 255)
RED = (128, 64, 64)
BLUE = (64,64,128)
# os.putenv('SDL_FBDEV', '/dev/fb1') # Target Display

pygame.init()
pygame.mouse.set_visible(False)
lcd = pygame.display.set_mode((800, 480))
lcd.fill((0, 0, 0))
pygame.display.update()

font_big = pygame.font.Font(font_file, 60)
font_small = pygame.font.Font(font_file, 60)
font_date = pygame.font.Font(font_file, 72)
font_time = pygame.font.Font(font_file, 160)
font_time_count = pygame.font.Font(font_file, 30)

font_hostname = pygame.font.Font(font_file, 60)
font_myip = pygame.font.Font(font_file, 60)
font_setting = pygame.font.Font(font_file, 60)
font_have_new_video = pygame.font.Font(font_file, 60)

font_env_get_time = pygame.font.Font(font_file, 60)
font_env_count = pygame.font.Font(font_file, 30)

font_cpu_temp = pygame.font.Font(font_file, 60)


def get_env(sleeptime, *args):
    global env_text
    global env_get_time
    global env_count
    while True:
        env_text = subprocess.check_output(["sudo", "python", "/home/pi/Adafruit_Python_BMP/examples/simpletest.py"])
        env_text = env_text.strip()
        env_get_time = time.strftime('%X')
        env_count +=1
        time.sleep(sleeptime)

def update_LCD(time_now, date_now):
    global time_count 
    while True:
        time_now = time.strftime('%X')
        date_now = time.strftime('%x %w')
        tft_update(time_now, date_now)
        time_count +=0.1
        sleep(0.1)


def main():
    time_now = time.strftime('%X')
    date_now = time.strftime('%x %w')    
    thread.start_new_thread(get_env, (1, ""))
    thread.start_new_thread(update_LCD, (time_now, date_now))

    while True:
        sleep(1)


def tft_update(time_now, date_now):
    global count

    cpu_temp_raw_data = subprocess.check_output(["/opt/vc/bin/vcgencmd", "measure_temp"])
    get_cpu_temp = cpu_temp_raw_data.strip()

    lcd.fill((0, 0, 0))
    text_surface_time = font_time.render(u'%s' % time_now, True, WHITE)
    text_surface_time_count = font_time_count.render(u'%s' % time_count, True, BLUE)
    text_surface_date = font_date.render(u'%s' % date_now, True, WHITE)
    text_surface_env_text = font_small.render('%s' % env_text, True, WHITE)
    text_surface_env_get_time = font_env_get_time.render('%s' % env_get_time, True, RED)
    text_surface_env_count = font_env_count.render('%s' % env_count, True, BLUE)
    text_surface_cpu_temp = font_cpu_temp.render(u'%s' % get_cpu_temp, True, WHITE)

    rect_time = text_surface_time.get_rect(center=(400, 90))
    rect_time_count = text_surface_time_count.get_rect(center=(400,400))
    rect_date = text_surface_date.get_rect(center=(400, 200))
    rect_env_text = text_surface_env_text.get_rect(center=(400,270))
    rect_env_get_time = text_surface_env_get_time.get_rect(center=(600,340))

    rect_cpu_temp = text_surface_cpu_temp.get_rect(center=(240,340))

    rect_env_count = text_surface_env_count.get_rect(center=(400,430))

    lcd.blit(text_surface_time, rect_time)
    lcd.blit(text_surface_time_count, rect_time_count)
    lcd.blit(text_surface_date, rect_date)
    lcd.blit(text_surface_env_text, rect_env_text)
    lcd.blit(text_surface_env_get_time, rect_env_get_time)
    lcd.blit(text_surface_env_count, rect_env_count)
    lcd.blit(text_surface_cpu_temp, rect_cpu_temp)

    pygame.display.update()


if __name__ == '__main__':
    print ("Display info")
    main()
