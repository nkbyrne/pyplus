#!/usr/bin/env python
import requests
from urllib3.exceptions import InsecureRequestWarning
from pprint import pprint

"""Using the Python requests library, perform an HTTP GET on the base URL of the NetBox server (https://netbox.lasthop.io/api/). Ensure that you are not verifying the SSL certificate. Print the HTTP status code, the response text, the JSON response, and the HTTP response headers. These items can be accessed using the following attributes/methods in the Python-requests Response object:"""

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

BASE_URL = "https://netbox.lasthop.io/api/"

http_headers = {}
http_headers["accept"] = "application/json; version=2.4;"
resp = requests.get(BASE_URL, headers=http_headers, verify=False)

print()
print(f"Response Code: {resp.status_code}")
print()
print("Response Text:")
pprint(resp.text)
print()
print("Response JSON:")
pprint(resp.json())
print()
print("Response Headers:")
pprint(dict(resp.headers))
print()

# retrieve the endpoints
BASE_URL = "https://netbox.lasthop.io/api/dcim/"
resp = requests.get(BASE_URL, headers=http_headers, verify=False)
print("Response JSON:")
pprint(resp.json())
print()
