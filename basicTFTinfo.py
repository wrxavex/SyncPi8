#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import os
import time
import platform
from time import sleep

import get_ip

my_ip = get_ip.myip

hostname = platform.node()
os.environ['TZ'] = 'Asia/Taipei'
time.tzset()

font_file = "/home/pi/SyncPi8/msjh.ttc"
os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()
pygame.mouse.set_visible(False)
lcd = pygame.display.set_mode((320, 240))
lcd.fill((255, 0, 0))
pygame.display.update()

WHITE = (255, 255, 255)

font_big = pygame.font.Font(font_file, 36)
font_small = pygame.font.Font(font_file, 36)
font_date = pygame.font.Font(font_file, 72)
font_hostname = pygame.font.Font(font_file, 24)
font_myip = pygame.font.Font(font_file, 24)


def tft_update(time_now):
    lcd.fill((0, 0, 0))
    text_surface_time = font_date.render(u'%s' % time_now, True, WHITE)
    text_surface_hostname = font_hostname.render(u'%s' % hostname, True, WHITE)
    text_surface_myip = font_myip.render(u'IP:%s' % my_ip, True, WHITE)

    rect = text_surface_time.get_rect(center=(160, 120))
    rect_hostname = text_surface_hostname.get_rect(center=(160, 18))
    rect_myip = text_surface_myip.get_rect(center=(160, 48))

    lcd.blit(text_surface_time, rect)
    lcd.blit(text_surface_hostname, rect_hostname)
    lcd.blit(text_surface_myip, rect_myip)

    pygame.display.update()


def main():
    while True:
        sleep(0.1)
        time_now = time.strftime('%X')
        tft_update(time_now)


if __name__ == '__main__':
    print ("Display info")
    main()

