#!/usr/bin/env python3
from jnpr.junos import Device
from getpass import getpass
from pprint import pprint

device = Device(host="srx2.lasthop.io", user="pyclass", password=getpass())
device.open()

print("Facts from {}:".format(device.facts["hostname"]))
pprint(device.facts)
