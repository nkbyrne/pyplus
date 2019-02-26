#!/usr/bin/env python
from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader([".", "./templates/"])

template_file = "ex3.j2"
template = env.get_template(template_file)

vrfs = [
    {
        "vrf_name": "blue",
        "rd_number": "100:1",
        "ipv4_enabled": True,
        "ipv6_enabled": False,
    },
    {
        "vrf_name": "red",
        "rd_number": "100:1",
        "ipv4_enabled": True,
        "ipv6_enabled": True,
    },
    {
        "vrf_name": "green",
        "rd_number": "100:3",
        "ipv4_enabled": False,
        "ipv6_enabled": True,
    },
    {
        "vrf_name": "orange",
        "rd_number": "100:4",
        "ipv4_enabled": False,
        "ipv6_enabled": False,
    },
    {
        "vrf_name": "black",
        "rd_number": "100:5",
        "ipv4_enabled": False,
        "ipv6_enabled": True,
    },
]

for vrf in vrfs:
    output = template.render(**vrf)
    print(output)
