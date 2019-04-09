#!/usr/bin/env python
import time
from concurrent.futures import ThreadPoolExecutor, wait
from my_devices import network_devices
from my_functions import ssh_command2
""" Create a new function that is a duplicate of your "ssh_command" function.
Name this function "ssh_command2". This function should eliminate all printing
to standard output and should instead return the show command output. Note, in
general, it is problematic to print in the child thread as you can get into race
conditions between the threads. Using the "ThreadPoolExecutor" in Concurrent
Futures execute "show version" on each of the devices defined in my_devices.py.
Use the 'wait' method to ensure all of the futures have completed. Concurrent
futures should be executing the ssh_command2 function in the child threads.
Print the total execution time required to accomplish this task."""

max_threads = 4
pool = ThreadPoolExecutor(max_threads)


def main():
    start_time = time.time()
    future_list = []
    for device in network_devices:
        future = pool.submit(ssh_command2, device, "show version")
        future_list.append(future)

    # Waits until all the pending threads are done
    wait(future_list)

    for future in future_list:
        print("Result: " + future.result())
    end_time = time.time()
    print("Finished in {} seconds".format(end_time - start_time))


if __name__ == "__main__":
    main()
