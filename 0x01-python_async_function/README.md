 # 0x01. Python - Async

## Description

This project is an introduction to asynchronous programming in Python. It covers the basic concepts of async and await, event loops, and how to handle asynchronous operations in Python. Asynchronous programming allows for more efficient execution of tasks, particularly I/O-bound operations, by enabling the program to perform other tasks while waiting for operations to complete.

## Learning Objectives

- Understand the basics of asynchronous programming.
- Learn how to use async and await in Python.
- Become familiar with event loops and how they work.
- Handle asynchronous operations and manage concurrency.
- Implement asynchronous functions and utilize asyncio for better performance in I/O-bound tasks.

## Requirements
- Python 3.7 or higher
- asyncio module
- Code editor or IDE (e.g., VSCode, PyCharm)

## Project Structure

The project consists of several tasks to practice asynchronous programming concepts:

0-basic_async_syntax.py - Introduction to async and await syntax.

1-async_comprehension.py - Using async comprehensions to handle asynchronous operations.

2-measure_runtime.py - Measuring the runtime of asynchronous functions.

3-concurrent_coroutines.py - Running multiple coroutines concurrently.

4-gather_with_concurrency.py - Using asyncio.gather to manage concurrency.

5-wait_random.py - Creating asynchronous functions that wait for a random amount of time.

## Installation

- Clone the repository:

git clone https://github.com/yourusername/0x01-python-async.git

- Navigate to the project directory:

cd 0x01-python-async

- Ensure you have Python 3.7 or higher installed. You can check your Python version using:

python3 --version

## Usage

To run any of the Python scripts, use the following command:

- python3 script_name.py
Replace script_name.py with the name of the script you want to execute.

## Example

Here's a simple example of an asynchronous function that waits for a random amount of time:

import asyncio

import random

async def wait_random(max_delay: int = 10):

    delay = random.uniform(0, max_delay)

    await asyncio.sleep(delay)

    return delay

# Running the asynchronous function
async def main():

    result = await wait_random()

    print(f"Waited for {result:.2f} seconds")

# Execute the main function
asyncio.run(main())

## Resources

- Python asyncio documentation
- PEP 492 – Coroutines with async and await syntax

## Author

- Your Name - GitHub Profile
