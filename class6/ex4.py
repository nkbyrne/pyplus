#!/usr/bin/env python3
import yaml
import pyeapi
from getpass import getpass
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from pprint import pprint

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")
template_file = "ex4.j2"
template = env.get_template(template_file)

filename = "aristas.yml"
with open(filename, "r") as f:
    devices = yaml.load(f)

password = getpass()

for device in devices.items():
    device[1]["password"] = password
    conn = pyeapi.client.connect(**device[1])
    api_device = pyeapi.client.Node(conn)
    jinja_config = device[1]["data"]
    config = template.render(**jinja_config)
    config = config.splitlines()
    output = api_device.config(config)
    print(output)


for device in devices.items():
    device[1]["password"] = password
    conn = pyeapi.client.connect(**device[1])
    api_device = pyeapi.client.Node(conn)
    output = api_device.enable("show ip interface brief")
    print("-" * 80)
    print(device[1]["host"])
    pprint((output[0]["result"]["output"]))
    print("-" * 80)
    print()
