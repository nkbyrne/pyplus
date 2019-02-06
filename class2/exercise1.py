#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_ios",
}

net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())

output = net_connect.send_command(
    "ping", expect_string=r"Protocol", strip_command=False
)
output += net_connect.send_command("\n", expect_string=r"Target", strip_command=False)
output += net_connect.send_command(
    "8.8.8.8", expect_string=r"Repeat", strip_command=False
)
output += net_connect.send_command("\n", expect_string=r"Datagram", strip_command=False)
output += net_connect.send_command("\n", expect_string=r"Timeout", strip_command=False)
output += net_connect.send_command("\n", expect_string=r"Extended", strip_command=False)
output += net_connect.send_command("\n", expect_string=r"Sweep", strip_command=False)
output += net_connect.send_command("\n", expect_string=r"sequence", strip_command=False)

print(output)

net_connect.disconnect()
