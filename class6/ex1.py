#!/usr/bin/env python
from __future__ import unicode_literals, print_function
import pyeapi
from getpass import getpass

connection = pyeapi.client.connect(
    transport="https",
    host="arista8.lasthop.io",
    username="pyclass",
    password=getpass(),
    port="443",
)

# enable = getpass("Enable: ")
# device = pyeapi.client.Node(connection, enablepwd=enable)
device = pyeapi.client.Node(connection)
output = device.enable(["show ip arp"])
# output = output[0]
# output = output['result']
# output = output['ipV4Neighbors']
output = output[0]["result"]["ipV4Neighbors"]

print()
for address in output:
    print("IP: {:13} MAC: {}".format(address["address"], address["hwAddress"]))
print()
