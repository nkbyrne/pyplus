#!/usr/bin/env python3
import sys
from jnpr.junos import Device
from jnpr.junos.exception import LockError
from jnpr.junos.utils.config import Config
from jnpr_devices import srx2


def check_connected(device):
    print()
    if device.connected:
        print("Connected to {}".format(device.hostname))
        return device.connected
    else:
        print("Unable to connect to {}".format(device.hostname))
        sys.exit(1)


def lock_device(device, cfg):
    try:
        cfg.lock()
    except LockError:
        print("Unable to obtain lock")
        sys.exit(1)


def load_config(device, cfg):
    return cfg.load("set system host-name pythononaplane", format="set", merge=True)


def rollback_config(device, cfg):
    return cfg.rollback(0)


def diff_config(device, cfg):
    print(cfg.diff())


if __name__ == __name__:
    device = Device(**srx2)
    device.open()
    cfg = Config(device)

    check_connected(device)
    lock_device(device, cfg)
    load_config(device, cfg)
    print("Changes to be made:")
    diff_config(device, cfg)
    rollback_config(device, cfg)
    print("Rolled back, changes to to made:")
    diff_config(device, cfg)
