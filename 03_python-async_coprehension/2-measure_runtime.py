#!/usr/bin/env python3
"""
Task 2
Import async_comprehension, write a measure_runtime coroutine that will
execute async_comprehension four times in parallel using asyncio.gather.
measure_runtime should measure the total runtime and return it.
"""

from time import perf_counter
from asyncio import gather
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Coroutine that will executes async_comprehension 4 times in parallel"""
    start_time = perf_counter()
    tasks = [async_comprehension() for task in range(4)]
    await gather(*tasks)
    end_time = perf_counter()
    total_tme = end_time - start_time
    return total_tme
