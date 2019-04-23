#!/usr/bin/env python3
import sys
from jnpr.junos import Device
from jnpr.junos.op.arp import ArpTable
from jnpr.junos.op.routes import RouteTable
from jnpr_devices import srx2
from pprint import pprint


def check_connected(device):
    print()
    if device.connected:
        print("Connected to {}".format(device.hostname))
        return device.connected
    else:
        print("Unable to connect to {}".format(device.hostname))
        sys.exit(1)


def gather_routes(device):
    routes_table = RouteTable(device)
    return routes_table.get()


def gather_arp_table(device):
    arp_table = ArpTable(device)
    return arp_table.get()


def print_output(dev, routes, arp):
    print()
    print("-" * 60)
    device = {}
    device["hostname"] = dev.hostname
    device["connected_port"] = dev.port
    device["connected_user"] = dev.user
    device["route_table"] = routes.items()
    device["arp_table"] = arp.items()
    pprint(device)
    print()


# def print_output():
#    print()
#    print("-" * 60)
#    print("Hostname: {}".format(device.hostname))
#    print("NETCONF Port: {}".format(device.port))
#    print("Username: {}".format(device.user))
#    print("-" * 60)
#    print("Route Table:")
#    for route in gather_routes().items():
#        print(route)
#    print("-" * 60)
#    print("ARP Table:")
#    for route in gather_routes().items():
#        print(route)
#    print("-" * 60)


if __name__ == "__main__":
    device = Device(**srx2)
    device.open()

    check_connected(device)
    routes = gather_routes(device)
    arp = gather_arp_table(device)

    print_output(device, routes, arp)
