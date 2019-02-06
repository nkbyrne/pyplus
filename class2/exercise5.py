#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint
from netmiko import ConnectHandler
from getpass import getpass

#device_password = getpass()
device_password = "88newclass"

cisco3 = {
    "host": "cisco3.lasthop.io",
    "device_type": "cisco_ios",
    "username": "pyclass",
    "password": device_password
}

cisco4 = {
    "host": "cisco4.lasthop.io",
    "device_type": "cisco_ios",
    "username": "pyclass",
    "password": device_password
}

arista1 = {
    "host": "arista1.lasthop.io",
    "device_type": "arista_eos",
    "username": "pyclass",
    "password": device_password
}

arista2 = {
    "host": "arista2.lasthop.io",
    "device_type": "arista_eos",
    "username": "pyclass",
    "password": device_password
}

arista3 = {
    "host": "arista3.lasthop.io",
    "device_type": "arista_eos",
    "username": "pyclass",
    "password": device_password
}

arista4 = {
    "host": "arista4.lasthop.io",
    "device_type": "arista_eos",
    "username": "pyclass",
    "password": device_password
}

nxos1 = {
    "host": "nxos1.lasthop.io",
    "device_type": "cisco_nxos",
    "username": "pyclass",
    "password": device_password
}

nxos2 = {
    "host": "nxos2.lasthop.io",
    "device_type": "cisco_nxos",
    "username": "pyclass",
    "password": device_password
}

alldevices = (nxos1, nxos2)
for device in alldevices:
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())
    output = net_connect.send_config_from_file(config_file='mychanges.txt')
    print(output)
    save_out = net_connect.save_config()
    print(save_out)
    net_connect.disconnect()
