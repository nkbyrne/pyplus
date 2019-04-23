#!/usr/bin/env python
import requests
import os
import json
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

"""Use an HTTP DELETE and Python-requests to delete the IP address object that
you just created. Remember to reference the ID of your object"""

address_id = "65"
BASE_URL = f"https://netbox.lasthop.io/api/ipam/ip-addresses/{address_id}/"

# Set the token based on the NETBOX_TOKEN environment variable
token = os.environ["NETBOX_TOKEN"]

http_headers = {}
http_headers["Content-Type"] = "application/json; version=2.4;"
http_headers["accept"] = "application/json; version=2.4;"
http_headers["Authorization"] = f"Token {token}"

resp = requests.delete(BASE_URL, headers=http_headers, verify=False)

print()
print(f"Response Code: {resp.status_code}")
print()
