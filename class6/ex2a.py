#!/usr/bin/env python
from __future__ import unicode_literals, print_function
import pyeapi
import yaml
from getpass import getpass

password = getpass()

with open("devices.yml") as f:
    devices = yaml.load(f)


for _, device_dict in devices.items():
    device_dict["password"] = password
    connection = pyeapi.connect(**device_dict)
    device = pyeapi.client.Node(connection)
    output = device.enable(["show ip arp"])
    output = output[0]["result"]["ipV4Neighbors"]
    print()
    for address in output:
        print("IP: {:13} {:5} MAC: {}".format(address["address"], "--->", address["hwAddress"]))
print()
