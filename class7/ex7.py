#!/usr/bin/env python3
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from getpass import getpass
from nxapi_plumbing import Device
from lxml import etree
from pprint import pprint

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

device = Device(
    api_format="xml",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=getpass(),
    transport="https",
    port=8443,
    verify=False,
)

command = device.show("show interface Ethernet2/1")
# print(etree.tostring(command).decode())
#interface = command.find(".//{*}interface").text
#state = command.find(".//{*}state").text
#mtu = command.find(".//{*}eth_mtu").text
#print("Interface: {}; State: {}; MTU: {}".format(interface, state, mtu))

print("Interface: {}; State: {}; MTU: {}"
      .format(command.find(".//{*}interface").text,
              command.find(".//{*}state").text,
              command.find(".//{*}eth_mtu").text))

commands = ["show system uptime", "show system resources"]

for cmd in commands:
    print()
    print(etree.tostring(device.show(cmd)).decode())
    print()

config_commands = [
    "interface loopback180",
    "description loopback180",
    "no shutdown",
    "interface loopback181",
    "description loopback181",
    "no shutdown",
]

output = device.config_list(config_commands)
for responce in output:
    print(etree.tostring(responce).decode())
