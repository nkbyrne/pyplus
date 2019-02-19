Value INTERFACE_NAME (\S+)
Value LINE_STATUS (\S+)
Value ADMIN_STATE (\S+)
Value MAC_ADDRESS (\S+)
Value MTU (\S+)
Value DUPLEX ((full|half)-duplex)
Value SPEED (\S+)

Start
  ^${INTERFACE_NAME} is ${LINE_STATUS}
  ^admin state is ${ADMIN_STATE}
  ^  Hardware.*bia\s${MAC_ADDRESS}
  ^  MTU\s${MTU}
  ^  ${DUPLEX}, ${SPEED}

