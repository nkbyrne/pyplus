Value Filldown BGP_ROUTER_ID (\d+\.\d+\.\d+\.\d+)
Value Filldown LOCAL_AS (\d+)
Value NEIGHBOR (\d+\.\d+\.\d+\.\d+)
Value REMOTE_AS (\d+)
Value UP_DOWN ((never|\d+.\d+.))
Value STATE_PREFIX_RCVD (\S+)



Start
  ^BGP router identifier ${BGP_ROUTER_ID}, local AS number ${LOCAL_AS}\s*$$
  ^Neighbor.*PfxRcd\s*$$ -> bgp

bgp
  ^${NEIGHBOR}\s+\d\s+${REMOTE_AS}\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+${UP_DOWN}\s+${STATE_PREFIX_RCVD} -> Record

