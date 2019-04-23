#!/usr/bin/env python3
import xmltodict

with open("show_security_zones.xml", "r") as f:
    sz = xmltodict.parse(f.read())


zones = sz["zones-information"]["zones-security"]

print("-" * 30)
for tally, zone in enumerate(zones):
    print(("Security Zone #{} {}").format(tally + 1, zone["zones-security-zonename"]))

print("-" * 30)
