"""
Subject : Practice handling synchronous functions with `asyncio` using `.run_in_executor()`
Author  : kimpro82
Date    : 2024.09.06

This module demonstrates how to perform asynchronous HTTP requests using the `requests` library for synchronous operations
and `asyncio` for asynchronous management. It includes:

1. `fetch_sync(url)`
    : A synchronous function that performs an HTTP GET request and measures the response time.
2. `fetch_async(loop, url)`
    : An asynchronous function that executes the synchronous `fetch_sync` function using `run_in_executor`.
3. `main(base_url, delay_time, n)`
    : The main asynchronous function that constructs URLs with a delay time, sends multiple requests concurrently,
      and prints the time taken for each request and the total execution time.

The script runs `n` concurrent requests to a URL constructed by combining `base_url` with a `delay_time` parameter
and measures the time taken for each request as well as the total time to complete all requests.
"""

import asyncio
import time
import requests

def fetch_sync(url):
    """
    Sends a synchronous HTTP GET request to the provided URL and measures the time taken for the request.

    Args:
        url (str): The URL to send the request to.

    Returns:
        float: The time taken for the HTTP request in seconds.
    """
    start_time = time.time()                # Record the start time
    _ = requests.get(url, timeout=100)       # The results are not needed
    elapsed_time = time.time() - start_time # Calculate elapsed time
    return elapsed_time

async def fetch_async(loop, url):
    """
    Asynchronously executes a synchronous HTTP request function using `run_in_executor`.

    Args:
        loop (asyncio.AbstractEventLoop): The event loop to run the task in.
        url (str): The URL to send the request to.

    Returns:
        float: The time taken for the HTTP request in seconds.
    """
    return await loop.run_in_executor(None, fetch_sync, url)

async def main(_base_url, _delay_time, _n):
    """
    The main asynchronous function that constructs the URLs and sends multiple requests concurrently,
    measuring and printing the time taken for each request and the total time for all requests.

    Args:
        _base_url (str): The base URL for the HTTP requests.
        _delay_time (int): The delay time to append to the base URL (used in URL path).
        _n (int): The number of requests to send.

    Returns:
        None
    """
    _loop = asyncio.get_event_loop()

    _url = f"{_base_url}/{_delay_time}"

    _tasks = [fetch_async(_loop, _url) for _ in range(_n)]

    _start_time = time.time()

    _results = await asyncio.gather(*_tasks)

    print(f"Tasks completed in {time.time() - _start_time:.2f} seconds")

    for _i, _elapsed_time in enumerate(_results, 1):
        print(f"Response {_i} took {_elapsed_time:.2f} seconds")

if __name__ == "__main__":
    BASE_URL = "https://httpbin.org/delay"
    DELAY_TIME = 3
    N = 10

    asyncio.run(main(BASE_URL, DELAY_TIME, N))
