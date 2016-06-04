id_file = open('/boot/set_id', 'r')
id_to_set = int(id_file.read())
id_file.close()

ip_config_file = open('/etc/dhcpcd.conf', 'r')
ip_config = ip_config_file.read()
ip_config_file.close()

if 0 < id_to_set > 255:
    new_ip_config = ip_config.replace('replace_id_here', 'id_to_set')
    ip_set_file = open('/etc/dhcpcd.conf', 'w')
    ip_set_file.write(new_ip_config)
    ip_set_file.close()








