import concurrent.futures


def odd_numbers():
    numbers = []
    for even in range(1, 20, 2):
        numbers.append(even)
    return numbers


def even_numbers():
    numbers = []
    for odd in range(2, 21, 2):
        numbers.append(odd)
    return numbers


def print_numbers(numbers):
    for number in numbers:
        print(number)


def start_threads_number():
    odd_number = odd_numbers()
    even_number = even_numbers()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(print_numbers, [odd_number, even_number])


if __name__ == "__main__":
    start_threads_number()
