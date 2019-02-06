#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

device = {
    "host": "cisco1.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_ios",
}

net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())


#cfg = [
#    'logging buffered 20000',
#    'no logging console',
#    ' clock timezone EST -5 0'
#]

output = net_connect.send_config_from_file(config_file='mychanges.txt')
#output = net_connect.send_config_set(cfg)
#output = net_connect.send_command("show ip int brief", use_textfsm=True)
print(output)

net_connect.disconnect()
