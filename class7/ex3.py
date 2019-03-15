#!/usr/bin/env python3
import xmltodict


def readxml(filename):
    with open(filename, "r") as f:
        xml = xmltodict.parse(f.read())
        return xml


def readxml_list(filename):
    with open(filename, "r") as f:
        xml = xmltodict.parse(f.read(), force_list={"zones-security": True})
        return xml


show_security_zones = readxml("show_security_zones.xml")
show_security_zones_trust = readxml("show_security_zones_trust.xml")
show_security_zones_trust_list = readxml_list("show_security_zones_trust.xml")
