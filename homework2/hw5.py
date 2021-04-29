from typing import Any, Iterable, List


def custom_range(
    array: Iterable, start: Any = 0, stop: Any = None, step: int = 1
) -> List:
    if start:
        start = array.index(start)
    if stop is None:
        stop, start = start, 0
    else:
        stop = array.index(stop)

    return list(array[start:stop:step])
