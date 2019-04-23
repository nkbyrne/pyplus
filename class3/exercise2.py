#!/usr/bin/env python
import yaml
from pprint import pprint

username = "admin"
password = "admin1234"

cisco3 = {
    "device_name": "cisco3",
    "host": "cisco3.lasthop.io",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

cisco4 = {
    "device_name": "cisco4",
    "host": "cisco4.lasthop.io",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

arista1 = {
    "device_name": "arista1",
    "host": "arista1.lasthop.io",
    "username": username,
    "password": password,
    "device_type": "arista_eos",
}

arista2 = {
    "device_name": "arista2",
    "host": "arista2.lasthop.io",
    "username": username,
    "password": password,
    "device_type": "arista_eos",
}

device_list = [cisco3, cisco4, arista1, arista2]

print(type(device_list))
pprint(device_list)

with open("exercise2.yaml", "w") as output:
    yaml.dump(device_list, output, default_flow_style=False)
