#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime


device = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_ios",
    "global_delay_factor": 2,
}

net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())

cfg = [
    'ip name-server 1.1.1.1',
    'ip name-server 1.0.0.1',
    'ip domain-lookup'
]

output = net_connect.send_config_set(cfg)
print(output)


net_connect.disconnect()
