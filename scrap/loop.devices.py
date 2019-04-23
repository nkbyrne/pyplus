#!/usr/bin/env python
import yaml
from netmiko import ConnectHandler

with open("/home/nbyrne/.netmiko.yml") as f:
    devices = yaml.load(f)

for device in ("cisco3", "cisco4"):
    net_connect = ConnectHandler(**devices[device])
    print(net_connect.find_prompt())
    net_connect.disconnect()
