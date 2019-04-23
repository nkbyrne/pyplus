from napalm import get_network_driver


def open_napalm_connection(dev):
    device_type = dev.pop("device_type")
    driver = get_network_driver(device_type)
    device = driver(**dev)
    device.open()
    return device


def create_backup(device):
    backup = device.get_config()
    filename = "{}_backup.txt".format(device.hostname)
    with open(filename, "w") as f:
        f.write(backup["running"])


def create_checkpoint(device):
    checkpoint = device.get_checkpoint_file()
