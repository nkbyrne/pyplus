#!/usr/bin/env python3
from lxml import etree

with open("show_security_zones.xml", "r") as f:
    sz = etree.fromstring(f.read())

trust_zone = sz[0]
print(trust_zone[0].text)
