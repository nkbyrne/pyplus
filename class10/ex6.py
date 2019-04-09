#!/usr/bin/env python
from concurrent.futures import ProcessPoolExecutor, as_completed
from my_devices import network_devices
from my_functions import ssh_command2
import pdb
"""Using a context manager, the ProcessPoolExecutor, and the map() method,
create a solution that executes "show ip arp" on all of the devices defined in
my_devices.py. Note, the Juniper device will require "show arp" instead of "show
ip arp" so your solution will have to properly account for this."""

max_threads = 4


def main():
    pdb.set_trace()
    with ProcessPoolExecutor(max_threads) as pool:
        cmd = []
        # gen the list of commands to pass to network devices in order for the "map"
        for device in network_devices:
            if "junos" in device["device_type"]:
                cmd.append("show arp")
            else:
                cmd.append("show ip arp")
        output = pool.map(ssh_command2, network_devices, cmd)
        for result in output:
            print()
            print("#" * 90)
            print(device["host"])
            print(result)
            print("#" * 90)
            print()


if __name__ == "__main__":
    main()
