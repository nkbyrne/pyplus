#!/usr/bin/env python
import time
from my_devices import network_devices
from my_functions import ssh_command
"""Create a Python script that executes "show version" on each of the network
devices defined in my_devices.py. This script should execute serially i.e. one
SSH connection after the other. Record the total execution time for the script.
Print the "show version" output and the total execution time to standard output.
As part of this exercise, you should create a function that both establishes a
Netmiko connection and that executes a single show command that you pass in as
argument. This function's arguments should be the Netmiko device dictionary and
the "show-command" argument. The function should return the result from the show
command."""

if __name__ == "__main__":
    start_time = time.time()
    for device in network_devices:
        output = ssh_command(device, "show version")
        print()
        print(output)
        print()
    end_time = time.time()
    print("Finished in {} seconds".format(end_time - start_time))
