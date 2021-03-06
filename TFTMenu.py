#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import os
import time
import platform
from time import sleep
import RPi.GPIO as GPIO

import get_ip
import NoButtonVideoSync as VS

my_ip = get_ip.myip


def read_sync_setting(filename):
    f = open(filename, 'r+w')
    return f.read().split()


player_setting = read_sync_setting('/boot/Sync_Setting.txt')

if 'ID=1' in player_setting:
    usb_video_file = 'video1.mp4'
if 'ID=2' in player_setting:
    usb_video_file = 'video2.mp4'
if 'ID=3' in player_setting:
    usb_video_file = 'video3.mp4'
if 'ID=4' in player_setting:
    usb_video_file = 'video4.mp4'
if 'ID=5' in player_setting:
    usb_video_file = 'video5.mp4'
if 'ID=6' in player_setting:
    usb_video_file = 'video6.mp4'
if 'ID=7' in player_setting:
    usb_video_file = 'video7.mp4'
if 'ID=8' in player_setting:
    usb_video_file = 'video8.mp4'


print usb_video_file

VS.VideoFileState(usb_video_file)
if VS.NewVideoFile:
    video_status = u'有新影片'
else:
    video_status = u'沒有新影片'

print VS.NewVideoFile

# Set timezone

hostname = platform.node()
os.environ['TZ'] = 'Asia/Taipei'
time.tzset()

font_file = "/home/pi/SyncPi8/msjh.ttc"

count = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
button_pre = 10
# Note #21 changed to #27 for rev2 Pi
button_map = {23: (255, 0, 0), 22: (0, 255, 0), 24: (0, 0, 255), 5: (0, 0, 0)}

# Setup the GPIOs as inputs with Pull Ups since the buttons are connected to GND
GPIO.setmode(GPIO.BCM)
for k in button_map.keys():
    GPIO.setup(k, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Colours
WHITE = (255, 255, 255)

os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()
pygame.mouse.set_visible(False)
lcd = pygame.display.set_mode((320, 240))
lcd.fill((0, 0, 0))
pygame.display.update()

font_big = pygame.font.Font(font_file, 36)
font_small = pygame.font.Font(font_file, 36)
font_date = pygame.font.Font(font_file, 24)
font_hostname = pygame.font.Font(font_file, 24)
font_myip = pygame.font.Font(font_file, 24)
font_setting = pygame.font.Font(font_file,24)
font_have_new_video = pygame.font.Font(font_file,24)


def button_check(k):
    global button_pre
    global count1
    global count2
    global count3
    global count4
    global video_status
    global usb_video_file
    if k == 23 and button_pre != 23:
        count1 += 1
        return count1
    if k == 22 and button_pre != 22:
        count2 += 1
        print ('Change Master or Slave')
        return count2
    if k == 24 and button_pre != 24:
        count3 += 1
        return count3
    if k == 5 and button_pre != 5:
        count4 += 1
        return count4
    else:
        return count


def main():
    global button_pre
    global video_status
    while True:
        # Scan the buttons
        for (k, v) in button_map.items():
            if not GPIO.input(k):
                count = button_check(k)
                if k == 23:
                    tft_check_button(u'影片更新鈕', count)
                    sleep(1)
                    time_now = time.strftime('%x %X')
                    if VS.NewVideoFile:
                        tft_update(time_now, 'Copying')
                        VS.SyncFile(usb_video_file)
                        tft_update(time_now, 'Copy Success, Video Updated')
                        video_status = u'剛剛更新了影片'
                        sleep(1)
                    else:
                        tft_update(time_now, u'沒有新影片')
                        video_status = u'沒有新影片'

                if k == 22:
                    tft_check_button(u'更改模式', count)
                if k == 5 or k == 24:
                    tft_check_button(u'未使用鈕', count)
        sleep(0.1)
        time_now = time.strftime('%x %X')
        tft_update(time_now, video_status)


def tft_check_button(k, count):
    lcd.fill((0,0,0))
    text_surface = font_big.render(u'按下%s' % k, True, WHITE)
    rect = text_surface.get_rect(center=(160, 120))
    lcd.blit(text_surface, rect)
    text_surface = font_small.render(u'按了%d次' % count, True, WHITE)
    rect = text_surface.get_rect(center=(240, 200))
    lcd.blit(text_surface, rect)
    pygame.display.update()
    time.sleep(0.5)


def tft_update(time_now, video_status):
    lcd.fill((0, 0, 0))
    text_surface_time = font_date.render(u'%s' % time_now, True, WHITE)
    text_surface_hostname = font_hostname.render(u'%s' % hostname, True, WHITE)
    text_surface_myip = font_myip.render(u'IP:%s' % my_ip, True, WHITE)
    text_surface_setting = font_setting.render(u'%s' % player_setting, True, WHITE)
    text_surface_have_new_video = font_have_new_video.render(u'%s' % video_status, True, WHITE)

    rect = text_surface_time.get_rect(center=(160, 200))
    rect_hostname = text_surface_hostname.get_rect(center=(160, 40))
    rect_myip = text_surface_myip.get_rect(center=(160, 80))
    rect_setting = text_surface_setting.get_rect(center=(160,120))
    rect_have_new_video = text_surface_have_new_video.get_rect(center=(160, 160))

    lcd.blit(text_surface_time, rect)
    lcd.blit(text_surface_hostname, rect_hostname)
    lcd.blit(text_surface_myip, rect_myip)
    lcd.blit(text_surface_setting,rect_setting)
    lcd.blit(text_surface_have_new_video, rect_have_new_video)

    pygame.display.update()


if __name__ == '__main__':
    print ("Display info")
    main()
