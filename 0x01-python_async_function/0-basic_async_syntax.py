#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that waits for a random delay.

The coroutine, `wait_random`, waits for a random delay up to a maximum limit
and returns the actual delay.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random number of seconds."""
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
