#!/usr/bin/env python3
"""
This module contains an asynchronous function that executes `wait_random`
multiple times concurrently.

The function, `wait_n`, concurrently executes `wait_random` for a specified
number of times and returns the delays in ascending order.
"""


import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Executes wait_random n times."""
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
