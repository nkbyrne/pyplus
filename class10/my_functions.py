from netmiko import ConnectHandler


def ssh_command(device, command):
    device = ConnectHandler(**device)
    output = device.send_command(command)
    print()
    print(output)
    print()
    device.disconnect()
    return


def ssh_command2(device, command):
    device = ConnectHandler(**device)
    output = device.send_command(command)
    device.disconnect()
    return output
