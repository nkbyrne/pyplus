#!/usr/bin/env python
from netmiko import ConnectHandler, file_transfer
from getpass import getpass

nxos1 = {
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_nxos",
}

source_file = "testx.txt"
dest_file = "testaa.txt"
direction = "get"
file_system = "bootflash:"

# create ssh connection
ssh_conn = ConnectHandler(**nxos1)
transfer_dict = file_transfer(
    ssh_conn,
    source_file=source_file,
    dest_file=dest_file,
    file_system=file_system,
    direction=direction,
    overwrite_file=True
)


print(transfer_dict)
