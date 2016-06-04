id_file = open('/boot/set_id', 'r')
id_to_set = id_file.read().strip()
print('id to set: %s' % id_to_set)
id_file.close()

ip_config_file = open('/home/pi/SyncPi8/ip_conf_sample', 'r')
ip_config = ip_config_file.read()
ip_config_file.close()


if 200 < int(id_to_set) < 255:
    new_ip_config = ip_config.replace('replace_id_here', id_to_set)
    ip_set_file = open('/etc/dhcpcd.conf', 'w')
    ip_set_file.write(new_ip_config)
    print("new config: %s" % new_ip_config)
    ip_set_file.close()
else:
    print('id not a valid number')

print('script done')






