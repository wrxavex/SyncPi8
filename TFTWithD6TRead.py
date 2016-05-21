#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import os
import time
import platform
from time import sleep
import RPi.GPIO as GPIO
import subprocess
import psutil
import json
import thread
import sys

try:
    import paho.mqtt.client as mqtt
except ImportError:
    import os
    import inspect
    cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"../src")))
    if cmd_subfolder not in sys.path:
        sys.path.insert(0, cmd_subfolder)
    import paho.mqtt.client as mqtt

D6T_blocks = ""

SHT31_Temperature = ""
SHT31_Humidity = ""

class MyMQTTClass:
    def __init__(self, clientid=None):
        self._mqttc = mqtt.Client(clientid)
        self._mqttc.on_message = self.mqtt_on_message
        self._mqttc.on_connect = self.mqtt_on_connect
        self._mqttc.on_publish = self.mqtt_on_publish
        self._mqttc.on_subscribe = self.mqtt_on_subscribe

    def mqtt_on_connect(self, mqttc, obj, flags, rc):
        print("rc: "+str(rc))

    def mqtt_on_message(self, mqttc, obj, msg):
        global D6T_blocks
        global SHT31_Temperature
        global SHT31_Humidity
        if "Temperature" in msg.topic:
            SHT31_Temperature = str(msg.payload)
        if "Humidity" in msg.topic:
            SHT31_Humidity = str(msg.payload)
        if "Blocks" in msg.topic:
            D6T_blocks = str(msg.payload)

        # print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

    def mqtt_on_publish(self, mqttc, obj, mid):
        print("mid: "+str(mid))

    def mqtt_on_subscribe(self, mqttc, obj, mid, granted_qos):
        print("Subscribed: "+str(mid)+" "+str(granted_qos))

    def mqtt_on_log(self, mqttc, obj, level, string):
        print(string)

    def run(self):
        self._mqttc.connect("www.znh.tw", 1883, 60)
        self._mqttc.subscribe("/#", 0)

        rc = 0
        while rc == 0:
            rc = self._mqttc.loop()
        return rc

lock = thread.allocate_lock() 


import get_ip
# import NoButtonVideoSync as VS

my_ip = get_ip.myip

# def read_sync_setting(filename):
#     f = open(filename, 'r+w')
#     return f.read().split()


# player_setting = read_sync_setting('/boot/Sync_Setting.txt')

# if 'ID=1' in player_setting:
#     usb_video_file = 'video1.mp4'
# if 'ID=2' in player_setting:
#     usb_video_file = 'video2.mp4'
# if 'ID=3' in player_setting:
#     usb_video_file = 'video3.mp4'
# if 'ID=4' in player_setting:
#     usb_video_file = 'video4.mp4'
# if 'ID=5' in player_setting:
#     usb_video_file = 'video5.mp4'
# if 'ID=6' in player_setting:
#     usb_video_file = 'video6.mp4'
# if 'ID=7' in player_setting:
#     usb_video_file = 'video7.mp4'
# if 'ID=8' in player_setting:
#     usb_video_file = 'video8.mp4'


# print usb_video_file

# VS.VideoFileState(usb_video_file)
# if VS.NewVideoFile:
#     video_status = u'有新影片'
# else:
#     video_status = u'沒有新影片'

# print VS.NewVideoFile

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
font_cpu_temp = pygame.font.Font(font_file, 24)
font_cpu_usage = pygame.font.Font(font_file, 24)
font_mqtt_temp = pygame.font.Font(font_file, 24)
font_mqtt_humi = pygame.font.Font(font_file, 24)
font_mqtt_D6T = pygame.font.Font(font_file, 24)


def env_status_now(filename):
    f = open(filename, 'r')
    text = f.readline()
    f.close()
    return text


# def button_check(k):
#     global button_pre
#     global count1
#     global count2
#     global count3
#     global count4
#     global video_status
#     global usb_video_file
#     if k == 23 and button_pre != 23:
#         count1 += 1
#         return count1
#     if k == 22 and button_pre != 22:
#         count2 += 1
#         print ('Change Master or Slave')
#         return count2
#     if k == 24 and button_pre != 24:
#         count3 += 1
#         return count3
#     if k == 5 and button_pre != 5:
#         count4 += 1
#         return count4
#     else:
#         return count


def main():
    # global button_pre
    # global video_status
    # while True:
    #     # Scan the buttons
    #     for (k, v) in button_map.items():
    #         if not GPIO.input(k):
    #             count = button_check(k)
    #             if k == 23:
    #                 tft_check_button(u'影片更新鈕', count)
    #                 sleep(1)
    #                 time_now = time.strftime('%x %X')
    #                 if VS.NewVideoFile:
    #                     tft_update(time_now, 'Copying')
    #                     VS.SyncFile(usb_video_file)
    #                     tft_update(time_now, 'Copy Success, Video Updated')
    #                     video_status = u'剛剛更新了影片'
    #                     sleep(1)
    #                 else:
    #                     tft_update(time_now, u'沒有新影片')
    #                     video_status = u'沒有新影片'

    #             if k == 22:
    #                 tft_check_button(u'更改模式', count)
    #             if k == 5 or k == 24:
    #                 tft_check_button(u'未使用鈕', count)
        sleep(0.1)
        time_now = time.strftime('%x %X')
        video_status = False
        thread.start_new_thread(tft_updater, (time_now, video_status))
        thread.start_new_thread(get_MQTT, ("", lock))
        while True:
            sleep(1)


def get_MQTT(sleeptime, *args):
    global MQTT_rc
    mqttc = MyMQTTClass()
    MQTT_rc = mqttc.run()


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


def tft_updater(timenow, date_now):
    while True:
        time_now = time.strftime('%X')
        date_now = time.strftime('%x %w')
        tft_update(time_now, date_now)
        sleep(0.016)    


def tft_update(time_now, video_status):
    global SHT31_Temperature
    global SHT31_Humidity
    global D6T_blocks

    CPU_usage = psutil.cpu_percent(interval = .5)

    D6T_blocks_list = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
    D6T_json = json.loads(D6T_blocks)
    print (D6T_json["1"])


    pygame.draw.rect(lcd, WHITE, (180,125, 40, 40), 10)




    D6T_Line1 = ""
    D6T_Line2 = ""
    D6T_Line3 = ""
    D6T_Line4 = ""


    # D6T_blocks_list = D6T_blocks.split(", ")
    # D6T_blocks_list[0] = D6T_blocks_list[0][1:]
    # D6T_blocks_list = list(reversed(D6T_blocks_list))

    # print (D6T_blocks_list)
    # print (D6T_blocks_list[4:8])
    # print (D6T_blocks_list[8:12])
    # print (D6T_blocks_list[12:16])
    # print D6T_blocks

    cpu_temp_raw_data = subprocess.check_output(["/opt/vc/bin/vcgencmd", "measure_temp"])
    get_cpu_temp = cpu_temp_raw_data.strip()
    lcd.fill((0, 0, 0))
    text_surface_time = font_date.render(u'%s' % time_now, True, WHITE)
    text_surface_hostname = font_hostname.render(u'%s' % hostname, True, WHITE)
    text_surface_myip = font_myip.render(u'IP:%s' % my_ip, True, WHITE)
    text_surface_cpu_temp = font_cpu_temp.render(u'CPU:%s' % get_cpu_temp[5:], True, WHITE)
    text_surface_cpu_usage = font_cpu_usage.render(u'Usage:%s' % CPU_usage, True, WHITE)
    text_surface_mqtt_temp = font_mqtt_temp.render(u'室溫:%s' % SHT31_Temperature, True, WHITE)
    text_surface_mqtt_humi = font_mqtt_humi.render(u'室濕:%s' % SHT31_Humidity, True, WHITE)
    # text_surface_mqtt_D6T_Line1 = font_mqtt_D6T.render(u'%s' % D6T_blocks_list[13:17], True, WHITE)
    # text_surface_mqtt_D6T_Line2 = font_mqtt_D6T.render(u'%s' % D6T_blocks_list[9:13], True, WHITE)
    # text_surface_mqtt_D6T_Line3 = font_mqtt_D6T.render(u'%s' % D6T_blocks_list[5:9], True, WHITE)
    # text_surface_mqtt_D6T_Line4 = font_mqtt_D6T.render(u'%s' % D6T_blocks_list[1:5], True, WHITE)

    # text_surface_setting = font_setting.render(u'%s' % player_setting, True, WHITE)
    # text_surface_have_new_video = font_have_new_video.render(u'%s' % video_status, True, WHITE)


    rect_hostname = text_surface_hostname.get_rect(center=(160, 10))
    rect_myip = text_surface_myip.get_rect(center=(160, 40))
    rect_cpu_temp = text_surface_cpu_temp.get_rect(center=(80, 70))
    rect_cpu_usage = text_surface_cpu_usage.get_rect(center=(240, 70))
    rect_mqtt_temp = text_surface_mqtt_temp.get_rect(center=(80, 100))
    rect_mqtt_humi = text_surface_mqtt_humi.get_rect(center=(240, 100))
    # rect_mqtt_D6T_Line1 = text_surface_mqtt_D6T_Line1.get_rect(center=(180,125))
    # rect_mqtt_D6T_Line2 = text_surface_mqtt_D6T_Line2.get_rect(center=(180,150))
    # rect_mqtt_D6T_Line3 = text_surface_mqtt_D6T_Line3.get_rect(center=(180,175))
    # rect_mqtt_D6T_Line4 = text_surface_mqtt_D6T_Line4.get_rect(center=(180,200))
    # rect_setting = text_surface_setting.get_rect(center=(160,120))
    # rect_have_new_video = text_surface_have_new_video.get_rect(center=(160, 160))
    rect_time = text_surface_time.get_rect(center=(160, 220))
    
    lcd.blit(text_surface_hostname, rect_hostname)
    lcd.blit(text_surface_myip, rect_myip)
    lcd.blit(text_surface_cpu_temp, rect_cpu_temp)
    lcd.blit(text_surface_cpu_usage, rect_cpu_usage)
    lcd.blit(text_surface_time, rect_time)
    lcd.blit(text_surface_mqtt_temp, rect_mqtt_temp)
    lcd.blit(text_surface_mqtt_humi, rect_mqtt_humi)
    # lcd.blit(text_surface_mqtt_D6T_Line1, rect_mqtt_D6T_Line1)
    # lcd.blit(text_surface_mqtt_D6T_Line2, rect_mqtt_D6T_Line2)
    # lcd.blit(text_surface_mqtt_D6T_Line3, rect_mqtt_D6T_Line3)
    # lcd.blit(text_surface_mqtt_D6T_Line4, rect_mqtt_D6T_Line4)
    # lcd.blit(text_surface_setting,rect_setting)
    # lcd.blit(text_surface_have_new_video, rect_have_new_video)

    pygame.display.update()


if __name__ == '__main__':
    print ("Display info")
    main()
