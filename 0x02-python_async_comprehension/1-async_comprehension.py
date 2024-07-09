#!/usr/bin/env python3
"""
Module contains a coroutine uses an async comprehension
"""


from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Collect random numbers using an async comprehension.

    Returns:
        List[float]: The list of 10 random numbers.
    """
    return [i async for i in async_generator()]
