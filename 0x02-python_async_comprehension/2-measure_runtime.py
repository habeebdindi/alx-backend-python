#!/usr/bin/env python3
"""This module contains a coroutine
"""
import time
import random
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """execute async_comprehension four times in parallel using asyncio.gather
    """
    start = time.time()
    res = await asyncio.gather(async_comprehension(), async_comprehension(),
                               async_comprehension(), async_comprehension())
    end = time.time()
    return end - start
