#!/usr/bin/env python
import requests
import os
import json
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

""" Building on the script from exercise 4, add a description to the the IP
address object that you just created. Accomplish this using an HTTP PUT. The
HTTP PUT operation will require all of the mandatory fields in the object (in
this case, the "address" field). Print the status code and the response.json()
from your PUT operation. The HTTP PUT operation will use same URL as exercise 4b
(i.e. the URL of the newly created IP address object including its ID)."""

address_id = "65"
BASE_URL = f"https://netbox.lasthop.io/api/ipam/ip-addresses/{address_id}/"

# Set the token based on the NETBOX_TOKEN environment variable
token = os.environ["NETBOX_TOKEN"]

http_headers = {}
http_headers["Content-Type"] = "application/json; version=2.4;"
http_headers["accept"] = "application/json; version=2.4;"
http_headers["Authorization"] = f"Token {token}"

data = {"address": "192.0.2.82/32", "description": "Neil's"}

resp = requests.put(BASE_URL, headers=http_headers, data=json.dumps(data), verify=False)

print()
print(f"Response Code: {resp.status_code}")
print()
print("Response JSON:")
pprint(resp.json())
print()
