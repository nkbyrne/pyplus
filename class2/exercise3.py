#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime


device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_ios",
    "global_delay_factor": 2,
}

net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())

showvers = "sh ver"
showlldp = "show lldp neighbors"

version = net_connect.send_command(showvers, use_textfsm=True)
lldp = net_connect.send_command(showlldp, use_textfsm=True)

print("=" * 60)
print(version)
print("=" * 60)
print()
print("lldp is a ", type(lldp))
print("=" * 60)
print(lldp)
print("=" * 60)
print("port number on the HPE switch is: ", lldp[0]["neighbor_interface"])
print("HPE Switch Connection Port: {}".format(lldp[0]["neighbor_interface"]))
print()
net_connect.disconnect()
