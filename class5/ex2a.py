#!/usr/bin/env python
from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader([".", "./templates/"])

template_file = "ex2a.j2"
template = env.get_template(template_file)

nxos1 = {"interface": "Ethernet2/1", "ip_address": "10.1.100.1", "netmask": "24"}

nxos2 = {"interface": "Ethernet2/1", "ip_address": "10.1.100.2", "netmask": "24"}

devices = [nxos1, nxos2]

for device in devices:
    output = template.render(**device)
    print()
    print(output)
    print()
