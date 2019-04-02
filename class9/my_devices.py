from getpass import getpass

passwd = getpass()

cisco3 = dict(
    hostname="cisco3.lasthop.io",
    device_type="ios",
    username="pyclass",
    password=passwd,
)

arista1 = dict(
    hostname="arista1.lasthop.io",
    device_type="eos",
    username="pyclass",
    password=passwd,
)

nxos1 = {
    "hostname": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": passwd,
    "device_type": "nxos",
    "optional_args": {"port": 8443},
}

network_devices = [cisco3, arista1]
