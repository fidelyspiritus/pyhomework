from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = dict()

    def wrapped():
        pass

    def caching(*args):
        if args not in cache_dict:
            cache_dict[args] = func(*args)
        return cache_dict[args]
    return caching

