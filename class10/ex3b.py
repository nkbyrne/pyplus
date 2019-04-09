#!/usr/bin/env python
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from my_devices import network_devices
from my_functions import ssh_command2
""" Instead of waiting for all of the futures to complete, use "as_completed" to
print the future results as they come available. Reuse your "ssh_command2"
function to accomplish this. Once again use the concurrent futures
"ThreadPoolExecutor" and print the "show version" results to standard output.
Additionally, print the total execution time to standard output."""

max_threads = 4
pool = ThreadPoolExecutor(max_threads)


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
