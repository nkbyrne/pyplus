#!/usr/bin/env python
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from my_devices import network_devices
from my_functions import ssh_command2
"""Create a new program that completes the same task as Exercise 3b except using
multiple processes (i.e. a 'ProcessPoolExecutor')."""

max_threads = 4
pool = ProcessPoolExecutor(max_threads)


def main():
    start_time = time.time()
    future_list = []
    for device in network_devices:
        future = pool.submit(ssh_command2, device, "show version")
        future_list.append(future)

    for future in as_completed(future_list):
        print("Result: " + future.result())
    end_time = time.time()
    print("Finished in {} seconds".format(end_time - start_time))


if __name__ == "__main__":
    main()
