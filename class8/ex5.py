#!/usr/bin/env python3
from jnpr.junos import Device
from lxml import etree
from pprint import pprint
from jnpr_devices import srx2
from ex2 import check_connected

device = Device(**srx2)
device.open()
check_connected(device)

show_version = device.rpc.get_software_information()
print(etree.tostring(show_version, encoding="unicode"))

show_intf_terse_007 =
device.rpc.get_interface_information(interface_name="fe-0/0/7", terse=True,
        normalize=True)
print(etree.tostring(show_intf_terse_007, encoding="unicode",
      pretty_print=True))
