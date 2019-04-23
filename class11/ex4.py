#!/usr/bin/env python
import requests
import os
import json
from pprint import pprint
from urllib3.exceptions import InsecureRequestWarning

""" Using an HTTP POST and the Python-requests library, create a new IP address
in NetBox. This IP address object should be a /32 from the 192.0.2.0/24
documentation block. Print out the status code and the returned JSON."""

# Set the token based on the NETBOX_TOKEN environment variable
token = os.environ["NETBOX_TOKEN"]

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
BASE_URL = "https://netbox.lasthop.io/api/ipam/ip-addresses/"

http_headers = {}
http_headers["Content-Type"] = "application/json; version=2.4;"
http_headers["accept"] = "application/json; version=2.4;"
http_headers["Authorization"] = f"Token {token}"

data = {"address": "192.0.2.82/32"}

resp = requests.post(BASE_URL, headers=http_headers, data=json.dumps(data), verify=False)

print()
print(f"Response Code: {resp.status_code}")
print()
print("Response JSON:")
pprint(resp.json())
print()

"""Using the response data from the HTTP POST that created the IP address entry
in exercise 4a, capture the "id" of the newly created IP address object. Using
this ID, construct a new URL. Use this new URL and the HTTP GET method to
retrieve only the API information specific to this IP address"""

address_id = resp.json()["id"]
#ddress_id = "65"
BASE_URL = f"https://netbox.lasthop.io/api/ipam/ip-addresses/{address_id}/"

resp = requests.get(BASE_URL, headers=http_headers, verify=False)
pprint(resp.json())
