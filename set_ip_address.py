id_file = open('/boot/set_id', 'r')
id_to_set = int(id_file.read())
print('id to set: %s' % id_to_set)
id_file.close()

ip_config_file = open('/home/pi/ip_conf_sample', 'r')
ip_config = ip_config_file.read()
print('ip config: ' % ip_config)
ip_config_file.close()

if 0 < id_to_set > 255:
    new_ip_config = ip_config.replace('replace_id_here', 'id_to_set')
    print('new ip config:'% new_ip_config)
    ip_set_file = open('/etc/dhcpcd.conf', 'w')
    ip_set_file.write(new_ip_config)
    ip_set_file.close()








