### Multiprocessing with ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time

def square_number(number):
    time.sleep(2)
    return f"Square:{number**2}"

if __name__ == '__main__':
    numbers = [1,2,3,4,5,6,7,8,9,10]
    t = time.time()
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square_number, numbers)

    for result in results:
        print(result)

    final = time.time()
    print("Program Execution Time: ", final-t)