#!/usr/bin/env python
import yaml
import time
from netmiko import ConnectHandler
from pprint import pprint

with open("/home/nbyrne/.netmiko.yml") as f:
    devices = yaml.load(f)

for device in ('cisco3', 'cisco4'):
    net_connect = ConnectHandler(**devices[device])
    print(net_connect.find_prompt())
    net_connect.disconnect()
