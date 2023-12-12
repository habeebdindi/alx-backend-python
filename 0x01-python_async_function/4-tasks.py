#!/usr/bin/env python3
"""This module contains a coroutine
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times with the specified max_delay.
    """
    delays = []
    tasks = [task_wait_random(max_delay) for i in range(n)]
    for res in asyncio.as_completed(tasks):
        delays.append(await res)
    return delays
