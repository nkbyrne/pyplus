#!/usr/bin/env python3
from pprint import pprint
from my_devices import network_devices
from my_functions import open_napalm_connection, create_backup


if __name__ == "__main__":
    for dev in network_devices:
        device = open_napalm_connection(dev)
        config = "{}-loopbacks".format(device.hostname)
        device.load_merge_candidate(filename=config)
        print()
        print("-" * 30)
        print("Changes to be made to {}:".format(device.hostname))
        print(device.compare_config())
        print("-" * 30)
        device.commit_config()
        print("Changes applied, current diff:")
        print(device.compare_config())
