"""
Subject : Practice using `aiohttp` for asynchronous HTTP requests
Author  : kimpro82
Date    : 2024.09.06

This module demonstrates how to perform asynchronous HTTP requests using the `aiohttp` library
for asynchronous operations and `asyncio` for asynchronous management. It includes:

1. `fetch(url)`: An asynchronous function that performs an HTTP GET request and measures the response time.
2. `main(base_url, delay_time, n)`: The main asynchronous function that constructs URLs with a delay time,
    sends multiple requests concurrently, and prints the time taken for each request and the total execution time.

The script runs `n` concurrent requests to a URL constructed by combining `base_url` with a `delay_time` parameter
and measures the time taken for each request as well as the total time to complete all requests.
"""

import asyncio
import time
import aiohttp

async def fetch(url):
    """
    Asynchronously performs an HTTP GET request to the provided URL and measures the time taken for the request.

    Args:
        url (str): The URL to send the request to.

    Returns:
        float: The time taken for the HTTP request in seconds.
    """
    start_time = time.time()  # Record the start time
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            await response.text()  # Read the response to ensure completion
    elapsed_time = time.time() - start_time  # Calculate elapsed time
    return elapsed_time

async def main(base_url, delay_time, n):
    """
    The main asynchronous function that constructs the URLs and sends multiple requests concurrently,
    measuring and printing the time taken for each request and the total time for all requests.

    Args:
        base_url (str): The base URL for the HTTP requests.
        delay_time (int): The delay time to append to the base URL (used in URL path).
        n (int): The number of requests to send.

    Returns:
        None
    """
    url = f"{base_url}/{delay_time}"

    # Create `n` asynchronous tasks, each sending a request to the same URL.
    tasks = [fetch(url) for _ in range(n)]

    start_time = time.time()

    results = await asyncio.gather(*tasks)

    print(f"Tasks completed in {time.time() - start_time:.2f} seconds")

    for i, elapsed_time in enumerate(results, 1):
        print(f"Response {i} took {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    BASE_URL = "https://httpbin.org/delay"
    DELAY_TIME = 3
    N = 10

    asyncio.run(main(BASE_URL, DELAY_TIME, N))
