#!/usr/bin/env python3
"""
Task 0:
Write an asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random that waits
for a random delay between 0 and max_delay (included and float value)
seconds and eventually returns it.
"""
import random
import asyncio


async def wait_random(max_deley=10):
    deley = random.uniform(0, max_deley)
    await asyncio.sleep(deley)
    return deley
