#!/usr/bin/env python3
from lxml import etree

with open("show_security_zones.xml", "r") as f:
    sz = etree.fromstring(f.read())

trust_zone = sz[0]


# total_children = len(trust_zone) - 1
# x = 0
# while x <= total_children:
#    print(trust_zone.getchildren()[x].tag)
#    x += 1

for child in trust_zone:
    print(child.tag)
