#!/usr/bin/env python3
"""
This module contains an asynchronous generator.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    An asynchronous generator that yields random numbers.

    Returns:
        AsyncGenerator[float, None]: An asynchronous generator object.

    Yields:
        float: A random floating-point number in the range [0, 10).
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
