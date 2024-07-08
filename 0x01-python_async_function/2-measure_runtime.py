#!/usr/bin/env python3
"""
This module contains a function that measures the average runtime of the
`wait_n` function.

The function, `measure_time`, computes the average runtime of `wait_n`
over a specified number of runs.
"""

import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Computes the average runtime of wait_n."""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
