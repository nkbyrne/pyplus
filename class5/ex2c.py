#!/usr/bin/env python
from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from netmiko import ConnectHandler
import my_devices

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader([".", "./templates/"])

template_file = "ex2b.j2"
template = env.get_template(template_file)

nxos1_config = {
    "interface": "Ethernet2/1",
    "ip_address": "10.1.100.1",
    "netmask": "24",
    "local_as": "22",
    "peer_ip": "10.1.100.2",
    "remote_as": "22",

}
nxos2_config = {
    "interface": "Ethernet2/1",
    "ip_address": "10.1.100.2",
    "netmask": "24",
    "local_as": "22",
    "peer_ip": "10.1.100.1",
    "remote_as": "22",
}

nxos1 = my_devices.nxos1
nxos2 = my_devices.nxos2

for device in nxos1, nxos2:
    net_connect = ConnectHandler(**device)
    if device == nxos1:
        print(net_connect.find_prompt())
        config = template.render(nxos1_config)
        net_connect.send_config_set(config)
    elif device == nxos2:
        print(net_connect.find_prompt())
        config = template.render(nxos2_config)
        net_connect.send_config_set(config)
