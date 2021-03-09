"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    if len(Sequence) < 3:
        return False
    while len(Sequence) >= 3:
        first, second, third = Sequence[0], Sequence[1], Sequence[2]
        if third != first + second:
            return False
        Sequence = Sequence[1:]
    return True
