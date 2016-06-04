id_file = open('/boot/set_id', 'r')
id_to_set = id_file.read()
print('id to set: %d' % id_to_set)
id_file.close()

ip_config_file = open('/home/pi/ip_conf_sample', 'r')
ip_config = ip_config_file.read()
print('ip config: %s' % ip_config)
ip_config_file.close()

print(0 < int(id_to_set) > 255)

if 0 < int(id_to_set) > 255:
    new_ip_config = ip_config.replace('replace_id_here', 'id_to_set')
    print('new ip config: %s'% new_ip_config)
    ip_set_file = open('/etc/dhcpcd.conf', 'w')
    ip_set_file.write(new_ip_config)
    ip_set_file.close()
else:
    print('id not a valid number')

print('script done')






