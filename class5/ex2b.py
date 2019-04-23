#!/usr/bin/env python
from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader([".", "./templates/"])

template_file = "ex2b.j2"
template = env.get_template(template_file)

nxos1 = {
    "interface": "Ethernet2/1",
    "ip_address": "10.1.100.1",
    "netmask": "24",
    "local_as": "22",
    "peer_ip": "10.1.100.2",
    "remote_as": "22",
}

nxos2 = {
    "interface": "Ethernet2/1",
    "ip_address": "10.1.100.2",
    "netmask": "24",
    "local_as": "22",
    "peer_ip": "10.1.100.1",
    "remote_as": "22",
}

devices = [nxos1, nxos2]

for device in devices:
    output = template.render(**device)
    print(output)
