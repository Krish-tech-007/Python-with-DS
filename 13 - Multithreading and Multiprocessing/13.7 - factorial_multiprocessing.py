'''
Real World Example: Multiprocessing for CPU Bound Tasks
Scenario: Factorial calculations
Factorial calculation especially for large numbers involve significant computational work.
Multiprocessing can be used to distribute the workload across multiple CPU cores, improving performance.
'''

import multiprocessing 
import math
import sys
import time

# Increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

# function to compute factorial of a number
def compute_factorial(n):
    print("Computing factorial of {n}")
    result = math.factorial(n)
    print("Factorial of {n} is {result}")
    return result

if __name__ == '__main__':
    numbers = [5000,6000,7000,8000]
    t = time.time()

    # Create a pool of worker processes
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial, numbers)
    
    for result in results:
        print(result)
    final = time.time()
    print("Program Execution Time: ", final-t)