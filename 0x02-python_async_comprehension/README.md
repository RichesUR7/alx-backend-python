# 0x02. Python - Async Comprehension

This directory contains projects and exercises focused on asynchronous comprehension in Python. Asynchronous programming is a powerful feature in Python that allows for concurrent execution of tasks, improving efficiency and performance in programs that involve I/O-bound operations.

## Learning Objectives

By the end of this project, you should be able to:

- Understand the concept of asynchronous programming in Python.
- Use `async` and `await` syntax in Python.
- Write asynchronous comprehensions to simplify and enhance asynchronous code.
- Apply asynchronous generators for efficient and clean asynchronous programming.

## Requirements

- Python 3.7 or later
- A good understanding of basic Python concepts and syntax
- Familiarity with synchronous comprehensions and generators

## Project Structure

The project is organized into the following files:

- **0-async_comprehension.py**: A script demonstrating basic asynchronous comprehension.
- **1-async_generator.py**: A script showcasing the use of asynchronous generators.
- **2-measure_runtime.py**: A script measuring the runtime of asynchronous comprehensions.
- **3-multiple_async_comprehension.py**: A script combining multiple asynchronous comprehensions for more complex operations.

## Installation and Usage

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/yourrepository.git
    cd yourrepository/0x02-python-async_comprehension
    ```

2. **Run the scripts**:
    Each script can be run individually to see the asynchronous code in action. For example:
    ```bash
    python3 0-async_comprehension.py
    ```

## Examples

### 0-async_comprehension.py

```python
import asyncio

async def async_comprehension():
    return [i async for i in async_generator()]

async def async_generator():
    for i in range(10):
        await asyncio.sleep(1)
        yield i

if __name__ == "__main__":
    result = asyncio.run(async_comprehension())
    print(result)

This script demonstrates a basic asynchronous comprehension that collects values from an asynchronous generator.

## 1-async_generator.py


import asyncio
import random

async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)

async def main():
    async for value in async_generator():
        print(value)

if __name__ == "__main__":
    asyncio.run(main())
This script showcases an asynchronous generator that yields random integers.

## Author

- Your Name

## License

- This project is licensed under the MIT License - see the LICENSE file for details.
