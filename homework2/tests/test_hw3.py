from typing import Any, List

import pytest

from homework2.hw3 import combinations


def test_combinations():
    assert combinations([1, 2], [3, 4]) == [
        [1, 3],
        [1, 4],
        [2, 3],
        [2, 4],
    ]
