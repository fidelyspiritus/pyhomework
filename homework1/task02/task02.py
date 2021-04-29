"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    if len(data) < 3:
        return False
    if data[0] != 1 or data[0] != 0 and data[1] != 1:
        return False
    while len(data) >= 3:
        first, second, third = data[0], data[1], data[2]
        if third != first + second:
            return False
        data = data[1:]
    return True
