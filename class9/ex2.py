#!/usr/bin/env python3
from pprint import pprint
from my_devices import network_devices
from my_functions import open_napalm_connection, create_backup


if __name__ == "__main__":
    devlist = []
    for dev in network_devices:
        device = open_napalm_connection(dev)
        devlist.append(device)
        print()
        print("-" * 60)
        print("ARP Table of {}".format(dev["hostname"]))
        pprint(device.get_arp_table())
        try:
            device.get_ntp_peers()
            print("NTP Peers: {}".format(device.get_ntp_peers()))
        except NotImplementedError:
            print("Unable to read NTP peers")
        print("Creating Backup of {}".format(dev["hostname"]))
        create_backup(device)
        print("-" * 60)
        print()
    print("List of all device Objects: {}".format(devlist))
