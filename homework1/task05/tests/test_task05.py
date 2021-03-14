from typing import List

import pytest

from homework1.task05.task05 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["value", "parameter", "expected_result"],
    [([1, 3, -1, -3, 5, 3, 6, 7], 3, 16), ([9], 2, 9), ([0, 0, 0, 0, 0], 4, 0)],
)
def test_find_maximal_subarray_sum(
    value: List[int], parameter: int, expected_result: int
):
    actual_result = find_maximal_subarray_sum(value, parameter)
    assert actual_result == expected_result