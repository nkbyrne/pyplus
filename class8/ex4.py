#!/usr/bin/env python3
from jnpr.junos import Device
from jnpr.junos.exception import LockError
from jnpr.junos.utils.config import Config
from jnpr_devices import srx2
from pprint import pprint
from ex2 import check_connected, gather_routes

addconfigfile = "ex4_config.conf"
rmconfigfile = "ex4_rmconfig.conf"
device = Device(**srx2)


def load_config(dev):
    cfg = Config(dev)
    cfg.lock()
    cfg.load(path=addconfigfile, format="text", merge=True)
    cfg.commit()
    cfg.unlock()


def rm_config(dev):
    cfg = Config(dev)
    cfg.lock()
    cfg.load(path=rmconfigfile, format="text", merge=True)
    cfg.commit()
    cfg.unlock()


if __name__ == "__main__":
    # Open device
    device = Device(**srx2)
    device.open()
    check_connected(device)
    # gather and print current routing
    routes = gather_routes(device)
    print()
    print("-" * 60)
    print("Current Routing table:")
    pprint(routes.items())
    print("-" * 60)
    print()
    # load new config and print results
    load_config(device)
    routes = gather_routes(device)
    print()
    print("-" * 60)
    print("New Routing table:")
    pprint(routes.items())
    print("-" * 60)
    print()
    # Remove new config we just added
    rm_config(device)
    routes = gather_routes(device)
    print()
    print("-" * 60)
    print("Restored Routing table:")
    pprint(routes.items())
    print("-" * 60)
    print()
