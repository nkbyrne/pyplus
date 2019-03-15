#!/usr/bin/env python3
from lxml import etree

with open("show_security_zones.xml", "r") as f:
    sz = etree.fromstring(f.read())

print("-" * 30)
print("1st child using list indices")
print(sz[0].tag)
print("1st child using getchildren()")
print(sz.getchildren()[0].tag)
print("-" * 30)
