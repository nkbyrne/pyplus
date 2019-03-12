#!/usr/bin/env python
from __future__ import unicode_literals, print_function
import pyeapi
from getpass import getpass
from my_funcs import yaml_load_devices

devices = yaml_load_devices()
password = getpass()

for _, device_dict in devices.items():
    device_dict["password"] = password
    connection = pyeapi.connect(**device_dict)
    device = pyeapi.client.Node(connection)
    output = device.enable(["show ip route"])
    result = output[0]["result"]
    routes = result["vrfs"]["default"]["routes"]
    for route, data in routes.items():
        print("-" * 10)
        print(route)
        if data["routeType"] == "connected":
            print("routeType is", data["routeType"])
            print("-" * 10)
            print()
        else:
            print("routeType is", data["routeType"])
            print("Next hop is", data["vias"][0]["nexthopAddr"])
            print("-" * 10)
            print()
