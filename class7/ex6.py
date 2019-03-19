#!/usr/bin/env python3
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from getpass import getpass
from nxapi_plumbing import Device
from pprint import pprint as pp

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

device = Device(
    api_format="jsonrpc",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=getpass(),
    transport="https",
    port=8443,
    verify=False,
)

output = device.show("show interface Ethernet2/1")
output = output["TABLE_interface"]["ROW_interface"]
print("Interface: {}; State: {}; MTU: {}".format(output["interface"], output["state"], output["eth_mtu"]))
