#!/usr/bin/env python3
from lxml import etree

with open("show_security_zones.xml", "r") as f:
    sz = etree.fromstring(f.read())

print(sz)
print(type(sz))
