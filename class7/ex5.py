#!/usr/bin/env python3
from lxml import etree
from pprint import pprint as pp


def readxml(filename):
    with open(filename, "rb") as f:
        return etree.fromstring(f.read())


if __name__ == "__main__":
    filename = "show_version.xml"
    xml = readxml(filename)
    print("-" * 20)
    print("Namespace map of {}:".format(filename))
    pp(xml.nsmap)

    serial_number = xml.find(".//{*}proc_board_id")
    print("-" * 20)
    print("Serial Number:")
    print(serial_number.text)
