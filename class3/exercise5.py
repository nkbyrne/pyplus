#!/usr/bin/env python
import yaml
from os import path
from netmiko import ConnectHandler

home_dir = path.expanduser("~")
filename = path.join(home_dir, ".netmiko.yml")

with open(filename) as f:
    devices = yaml.load(f)


# for device in ('cisco3', ):
#    net_connect = ConnectHandler(**devices[device])
#    print(net_connect.find_prompt())
#    net_connect.disconnect()

cisco_devices = devices["cisco"]
for device in cisco_devices:
    net_connect = ConnectHandler(**devices[device])
    print(net_connect.find_prompt())
    net_connect.disconnect()
