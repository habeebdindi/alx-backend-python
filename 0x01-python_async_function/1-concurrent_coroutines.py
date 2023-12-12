#!/usr/bin/env python3
"""This module contains a coroutine
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[int]:
    """Spawns wait_random n times with the specified max_delay.
    """
    delays = []
    tasks = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    for res in asyncio.as_completed(tasks):
        delays.append(await res)
    return delays
