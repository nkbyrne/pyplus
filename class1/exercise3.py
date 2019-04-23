#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

device = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_ios",
}

print("Enter Password for", (device["host"]))

net_connect = ConnectHandler(**device)
output = net_connect.send_command("show version")

with open("output.txt", "w") as f:
    f.write(output)
