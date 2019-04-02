#!/usr/bin/env python3
from pprint import pprint
from my_devices import nxos1
from my_functions import open_napalm_connection, create_checkpoint

# Surpress SSL warnings
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

mydevice = nxos1

if __name__ == "__main__":
    device = open_napalm_connection(mydevice)
    getcheckpoint = device._get_checkpoint_file()
    filename = "{}_checkpoint.txt".format(device.hostname)
    with open(filename, "w") as f:
        f.write(getcheckpoint)
    device.load_replace_candidate("nxos1.lasthop.io_add_loopback.txt")
    print()
    print("Changes to be applied:")
    print(device.compare_config())
    print()
    print("Aborting change")
    device.discard_config()
    print("Changes staged (should be none):")
    print(device.compare_config())
