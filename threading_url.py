import datetime
import threading
import time
from multiprocessing import Process

import requests

urls = [
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/4",
    "https://httpbin.org/delay/3",
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/4",
    "https://httpbin.org/delay/5",
    "https://httpbin.org/delay/3",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/4",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/3",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/4",
    "https://httpbin.org/delay/5",
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/3",
    "https://httpbin.org/delay/5",
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/5",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/3",
]


def make_request(url, file_name):
    response = requests.get(url)
    response.raise_for_status()
    date_time = datetime.datetime.now()
    with open(file_name, "a") as file:
        file.write(f"Url: {url}, date: {date_time}\n")
        file.write(response.text + "\n")


def make_request_threading_url():
    threads = []
    for url in urls:
        thread = threading.Thread(target=make_request, args=(url, "threading_url.txt",))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def make_request_processing_url():
    process = []
    for url in urls:
        proces = Process(target=make_request, args=(url, "multiprocessing_url.txt",))
        process.append(proces)
        proces.start()

    for proces in process:
        proces.join()


if __name__ == "__main__":
    start_time = time.time()
    make_request_threading_url()
    end_time = time.time()
    time_work = end_time - start_time
    print(f"Time work threading: {time_work}")

    start_time = time.time()
    make_request_processing_url()
    end_time = time.time()
    time_work = end_time - start_time
    print(f"Time work multiprocessing: {time_work}")
