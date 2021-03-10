from typing import List

import pytest

from homework1.task05 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["value", "parameter", "expected_result"],
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
    ],
)
def test_find_maximal_subarray_sum(value: List[int], int, expected_result: int):
    actual_result = find_maximal_subarray_sum(value)
    assert actual_result == expected_result
