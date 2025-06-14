## Multiproccessing
## Processes that run in parallel

## When to use
## CPU Bound Tasks - Tasks that are heavy on CPU usage (eg: Mathematical compuatations, data proccessing)
## Parallel execution - Want to use multiple cores of the CPU

import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i ** 2}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube: {i ** 3}")

if __name__ == '__main__': #Entry point
    ## Create two processes 
    ## Run as independent processes
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)
    t = time.time()
    ## Start the process 
    p1.start()
    p2.start()

    ## Wait for the process to complete
    p1.join()
    p2.join()
    final = time.time()
    print("Program Execution Time: ", final-t)