#!/usr/bin/env python
import yaml
from os import path
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse

home_dir = path.expanduser("~")
filename = path.join(home_dir, ".netmiko.yml")

with open(filename) as f:
    devices = yaml.load(f)

device = "cisco4"
net_connect = ConnectHandler(**devices[device])
showrun = net_connect.send_command("show run")
showrunparsed = CiscoConfParse(showrun.splitlines())
inf = showrunparsed.find_objects_w_child(parentspec=r"^interface",
                                         childspec=r"^\s+ip address")

for interface in inf:
    print("#" * 60)
    print("Interface: {}".format(interface.text.split()[1]))
    ip_address = interface.re_search_children(r"ip address")[0].text
    ip = ip_address.split()[2]
    mask = ip_address.split()[3]
    # print("IP: {} {}".format(ip_address.split()[2], [3]))
    print("IP: {} {}".format(ip, mask))
    print("#" * 60)
net_connect.disconnect()
