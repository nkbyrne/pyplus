#!/usr/bin/env python
from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader([".", "./templates/"])

template_file = "ex5.j2"
template = env.get_template(template_file)


my_vars = {
    "ntp_server01": "130.126.24.24",
    "ntp_server02": "152.2.21.1",
    "timezone": "PST",
    "timezone_offset": "-8",
    "timezone_dst": "PDT",
}

output = template.render(**my_vars)
print(output)
