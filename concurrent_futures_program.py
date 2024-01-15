import time

import requests
import concurrent.futures


def make_request(url):
    response = requests.get(url)
    response.raise_for_status()
    print(response.json())


urls = ["https://httpbin.org/uuid"] * 30


def make_request_concurrent():
    with concurrent.futures.ThreadPoolExecutor(15) as executor:
        return executor.map(make_request, urls)


def request_url():
    for item in urls:
        response = requests.get(item)
        response.raise_for_status()
        print(response.json())


if __name__ == "__main__":
    start_time = time.time()
    make_request_concurrent()
    end_time = time.time()
    time_work = end_time - start_time

    start_time2 = time.time()
    request_url()
    end_time2 = time.time()
    time_work2 = end_time2 - start_time2

    print(f"Time work threading: {time_work}, time work standart: {time_work2}")
