#!/usr/bin/env python3
from lxml import etree


def readxml(filename):
    with open(filename, "r") as f:
        xml = etree.fromstring(f.read())
        return xml


show_security_zones = readxml("show_security_zones.xml")
zonesecurity = show_security_zones.find("zones-security")
allzonesecurity = show_security_zones.findall("zones-security")
children = zonesecurity.getchildren()

print()
print("Find tag of the first zones-security element")
print("-" * 30)
print(zonesecurity.tag)
print()
print("Find tag of all child elements of the first zones-security element")
for child in children:
    print(child.tag)

print("-" * 30)
print("Find first tag of zones-security-zonename")
print(children[0].text)
print("-" * 30)

print("-" * 30)
print("Find all zones-security zone names")
for zone in show_security_zones.findall("zones-security"):
    print(zone[0].text)
print("-" * 30)
