#!/usr/bin/env python
from jinja2 import Template


template = """router bgp {{ local_as }}
  neighbor {{ peer1_ip }} remote-as {{ peer1_ip_as }}
    update-source loopback99
    ebgp-multihop 2
    address-family ipv4 unicast
  neighbor {{ peer2_ip }} remote-as {{ peer2_ip_as }}
    address-family ipv4 unicast"""

my_vars = {
    "local_as": "10",
    "peer1_ip": "10.1.20.2",
    "peer1_ip_as": "20",
    "peer2_ip": "10.1.30.2",
    "peer2_ip_as": "30",
}

j2_template = Template(template)
output = j2_template.render(**my_vars)
print(output)
