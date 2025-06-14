### Multithreading

## When to use multithreading
## IO Bound Tasks - Tasks that spend more time waiting for IO operations (eg: file operations, network requests)
## Concurrent Execution - When we want to improve the throughput of our application by performing multiple operations concurrently.

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number: {i}")

def print_letters():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter: {letter}")

## Create 2 threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t = time.time()
#print_numbers()
#print_letters()

## Starting the thread
## When one thread is busy or sleeping, the other thread will get executed
t1.start()
t2.start()

### Wait for threads to complete
t1.join()
t2.join()
## Once both have executed, they will be joined back to the main thread

finished_time = time.time()
print(f"Program executed in {finished_time-t}")