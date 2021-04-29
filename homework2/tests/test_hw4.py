from typing import Any

from homework2.hw4 import cache


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)


def test_cache() -> Any:
    assert val_1 is val_2
