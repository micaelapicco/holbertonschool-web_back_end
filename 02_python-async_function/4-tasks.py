#!/usr/bin/env python3
"""
Task 4:
Take the code from wait_n and alter it into a new function task_wait_n
The code is nearly identical to wait_n except task_wait_random is being called.
"""
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """call wait n times"""
    list = []
    for i in range(n):
        wait = await(task_wait_random(max_delay))
        list.append(wait)
    return sorted(list)
