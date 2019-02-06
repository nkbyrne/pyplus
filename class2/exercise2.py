#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime


device = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_ios",
    "global_delay_factor": 2,
}

net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())

command = "show lldp neighbors detail"

starttime = datetime.now()
output1 = net_connect.send_command(command)
endtime = datetime.now()
print("-" * 60)
print(output1)
print("-" * 60)
print("\n\nExecution Time: {}".format(endtime - starttime))

starttime = datetime.now()
output2 = net_connect.send_command(command, delay_factor=8)
endtime = datetime.now()
print("-" * 60)
print(output2)
print("-" * 60)
print("\n\nExecution Time: {}".format(endtime - starttime))


net_connect.disconnect()
