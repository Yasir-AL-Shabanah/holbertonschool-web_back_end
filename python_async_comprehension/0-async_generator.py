#!/usr/bin/env python3
"""
This module defines a coroutine called async_generator that yields random numbers.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Loops 10 times, waits 1 second each time, then yields a random number
    between 0 and 10.

    Returns:
        AsyncGenerator[float, None]: An async generator yielding floats.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
