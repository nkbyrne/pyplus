Value DEVICE_ID (\S+)
Value LOCAL_INTF (Eth\d\/\d)
Value CAPABILITY (\S+)
Value PORT_ID (\S+)



Start
  ^Device.*Port ID\s*$$ -> lldp

lldp
  ^${DEVICE_ID}\s+${LOCAL_INTF}\s+\d+\s+${CAPABILITY}\s+${PORT_ID} -> Record

