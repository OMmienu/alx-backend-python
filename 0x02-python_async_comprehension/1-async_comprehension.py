#!/usr/bin/env python3
"""
Async_comprehension module
"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    returns random numbers generated by async_generator using the async for
    list comprehension syntax
    """
    return [val async for val in async_generator()]
