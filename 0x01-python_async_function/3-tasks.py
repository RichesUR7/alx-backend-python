#!/usr/bin/env python3
"""
This module contains a function that creates an asyncio Task for the
`wait_random` coroutine.

The function, `task_wait_random`, wraps the `wait_random` coroutine
in an asyncio Task and returns it.
"""

import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates an asynchronous task for wait_random."""
    return asyncio.create_task(wait_random(max_delay))
