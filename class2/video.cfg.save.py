#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint
device = {
    "host": "cisco1.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_ios",
    "fast_cli": True,
}

net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())

output = net_connect.send_config_from_file(config_file='mychanges.txt')
print(output)

save_out = net_connect.save_config()
print(save_out)

output = net_connect.send_command("show ip arp", use_textfsm=True)
pprint(output)

net_connect.disconnect()
