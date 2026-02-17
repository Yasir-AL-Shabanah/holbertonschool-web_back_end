#!/usr/bin/env python3
"""
This module contains the function task_wait_random
that returns an asyncio.Task object.
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes an integer max_delay and returns an asyncio.Task.

    Args:
        max_delay (int): The maximum delay for the wait_random function.

    Returns:
        asyncio.Task: The task that runs wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
