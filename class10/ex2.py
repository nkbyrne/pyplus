#!/usr/bin/env python
import time
import threading
from my_devices import network_devices
from my_functions import ssh_command
""" Create a new file named my_functions.py. Move your function from exercise1
to this file. Name this function "ssh_command". Reuse functions from this file
for the rest of the exercises. Complete the same task as Exercise 1b except this
    time use "legacy" threads to create a solution. Launch a separate thread for
    each device's SSH connection. Print the time required to complete the task
    for all of the devices. Move all of the device specific output printing to
        the called function (i.e. to the child thread)."""

def main():
    start_time = time.time()
    threads = []
    for device in network_devices:
        my_thread = threading.Thread(target=ssh_command, args=(device, "show \
                                     version"))
        threads.append(my_thread)
        my_thread.start()
    for thread in threads:
        thread.join()
    end_time = time.time()
    print("Finished in {} seconds".format(end_time - start_time))


if __name__ == "__main__":
    main()
