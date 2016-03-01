import pygame
import os

os.environ['TZ'] = 'Asia/Taipei'
time.tzset()

font_file = "/home/pi/SyncPi8/msjh.ttc"


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

def main():


        sleep(0.1)
        time_now = time.strftime('%x %X')
        tft_update(time_now, video_status)


if __name__ == '__main__':
    print ("Display info")
    main()
