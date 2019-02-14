#!/usr/bin/env python
import json

filename = "exercise4.json"
with open(filename) as f:
    arp_data = json.load(f)


my_dict = {}

arp = arp_data["ipV4Neighbors"]
for entry in arp:
    ip = entry["address"]
    mac = entry["hwAddress"]
    my_dict[ip] = mac

print(my_dict)
