#!/usr/bin/env python
from ciscoconfparse import CiscoConfParse

bgp_config = '''
router bgp 44
 bgp router-id 10.220.88.38
 address-family ipv4 unicast
 !
 neighbor 10.220.88.20
  remote-as 42
  description pynet-rtr1
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
  !
 !
 neighbor 10.220.88.32
  remote-as 43
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
'''

cisco_obj = CiscoConfParse(bgp_config.splitlines())
neighbors = cisco_obj.find_objects_w_child(
    pentspec=r"neighbor", childspec=r"^\s+remote-as")

bgp_list = []

for peers in neighbors:
    bgp_peer = peers.text.split()[1]
    remote = (peers.re_search_children(r"remote-as")[0].text)
    bgp_remote = (remote.split()[1])
    bgp_list.append(tuple((bgp_peer, bgp_remote)))

print("BGP Peers:")
print(bgp_list)
