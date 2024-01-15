import concurrent.futures
import math
import time


def calculator(number):
    time.sleep(2)
    return math.exp(number)


def start_threads_calculator(number=100):
    numbers = list(range(1, number))
    with concurrent.futures.ThreadPoolExecutor(50) as executor:
        return sum(executor.map(calculator, numbers))


def start_proces_calculator(number=100):
    numbers = list(range(1, number))
    with concurrent.futures.ProcessPoolExecutor(50) as executor:
        return sum(executor.map(calculator, numbers))


if __name__ == "__main__":
    start_time = time.time()
    suma = start_threads_calculator()
    end_time = time.time()
    time_work = end_time - start_time
    print(f"Suma: {suma}, time work: {time_work}")

    start_time = time.time()
    suma = start_proces_calculator()
    end_time = time.time()
    time_work = end_time - start_time
    print(f"Suma: {suma}, time work: {time_work}")
