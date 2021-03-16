from typing import Sequence

import pytest

from homework1.task02 import check_fibonacci


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ([0, 1, 1, 2, 3, 5], True),
        ([12, 3], False),
        ([0, 0, 0, 0], False),
    ],
)
def test_check_fibonacci(value: Sequence[int], expected_result: bool):
    actual_result = check_fibonacci(value)
    assert actual_result == expected_result