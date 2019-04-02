#!/usr/bin/env python3
from pprint import pprint
from napalm import get_network_driver
from my_devices import network_devices


def connection(dev):
    device_type = dev.pop("device_type")
    driver = get_network_driver(device_type)
    device = driver(**dev)
    device.open()
    return device


if __name__ == "__main__":
    # devlist = []
    for dev in network_devices:
        device = connection(dev)
        # devlist.append(device)
        print()
        print("{}:".format(dev["hostname"]))
        print("-" * 60)
        print("Device Object:")
        print(device)
        print("Device Facts:")
        pprint(device.get_facts())
        print()
        print("Device Platform: {}".format(device.platform))
        print("-" * 60)
