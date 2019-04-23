#!/usr/bin/env python
import requests
from urllib3.exceptions import InsecureRequestWarning
import os

""" Retrieve a list of all the devices in NetBox. This will require
authentication. As in the previous task, create your headers manually and pass
them into your request"""

# Set the token based on the NETBOX_TOKEN environment variable
token = os.environ["NETBOX_TOKEN"]

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
BASE_URL = "https://netbox.lasthop.io/api/dcim/devices"

http_headers = {}
http_headers["accept"] = "application/json; version=2.4;"
http_headers["Authorization"] = f"Token {token}"

resp = requests.get(BASE_URL, headers=http_headers, verify=False)

devices = resp.json()["results"]
result = []
for device in devices:
    print("-" * 60)
    #   result.append(device["display_name"])
    print(device["display_name"])
    print("-" * 10)
    print("Location: {}".format(device["site"]["name"]))
    print("Vendor: {}".format(device["device_type"]["manufacturer"]["name"]))
    print("Status: {}".format(device["status"]["label"]))
    print("-" * 60)
    print("\n \n")
