from typing import Callable


def cache(times: int):

    def wrapped(func: Callable) -> Callable:
        cache_dict = dict()

        def caching(*args):
            if args not in cache_dict or cache_dict[args][1] == 0:
                cache_dict[args] = [func(*args), times]
            cache_dict[args][1] -= 1
            return cache_dict[args][0]
        return caching
    return wrapped
