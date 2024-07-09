#!/usr/bin/env python3
"""
Module contains a coroutine that measures the total runtime.
"""

import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime.

    Returns:
        float: The total runtime.
    """
    start_time = time.time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.time()
    return end_time - start_time
