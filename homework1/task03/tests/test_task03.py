from typing import Tuple

import pytest

from homework1.task03 import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ("sample.txt", (1, 6, 4, 9, 2, 3, 4, 5)),
        ("sample0.txt", (0, 0)),
    ],
)
def test_find_maximum_and_minimum(value: str, expected_result: Tuple[int, int]):
    actual_result = find_maximum_and_minimum(value)
    assert actual_result == expected_result
