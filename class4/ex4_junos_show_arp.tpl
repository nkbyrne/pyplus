Value MAC_ADDRESS (([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))
Value ADDRESS (\S+)
Value NAME (\S+)
Value INTERFACE (\S+)



Start
  ^MAC.*Flags\s*$$ -> ShowARP

ShowARP
  ^${MAC_ADDRESS}\s+${ADDRESS}\s+${NAME}\s+${INTERFACE} -> Record

