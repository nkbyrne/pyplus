#!/usr/bin/env python3
from lxml import etree

with open("show_security_zones.xml", "r") as f:
    sz = etree.fromstring(f.read())

print("-" * 30)
print("XML root tag is:")
print(sz.tag)
print("It contains {} children".format(len(sz.getchildren())))
print("-" * 30)
