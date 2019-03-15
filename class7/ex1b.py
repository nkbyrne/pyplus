#!/usr/bin/env python3
from lxml import etree

with open("show_security_zones.xml", "r") as f:
    sz = etree.fromstring(f.read())

my_xml = etree.tostring(sz)

print(my_xml.decode())
