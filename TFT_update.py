def TFT_update():
        lcd.fill((0, 0, 0))

        text_surface = font_date.render(u'%s' % timenow, True, WHITE)
        text_surface_hostname = font_hostname.render(u'%s' % hostname, True, WHITE)
        text_surface_myip = font_myip.render(u'%s' % my_ip, True, WHITE)
        text_surface_setting = font_setting.render(u'%s' % player_setting, True, WHITE)
        text_surface_have_new_video = font_have_new_video.render(u'New Video is %s' % VS.NewVideoFile, True, WHITE)

        rect = text_surface.get_rect(center=(160, 200))
        rect_hostname = text_surface_hostname.get_rect(center=(160, 40))
        rect_myip = text_surface_myip.get_rect(center=(160, 80))
        rect_setting = text_surface_setting.get_rect(center=(160,120))
        rect_have_new_video = text_surface_have_new_video.get_rect(center=(160, 160))

        lcd.blit(text_surface, rect)
        lcd.blit(text_surface_hostname, rect_hostname)
        lcd.blit(text_surface_myip, rect_myip)
        lcd.blit(text_surface_setting,rect_setting)
        lcd.blit(text_surface_have_new_video, rect_have_new_video)

        pygame.display.update()