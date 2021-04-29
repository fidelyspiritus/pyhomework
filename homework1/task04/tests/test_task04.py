from typing import List

import pytest

from homework1.task04.task04 import check_sum_of_four


@pytest.mark.parametrize(
    ["a", "b", "c", "d", "expected_result"],
    [
        ([1, 2], [1, 2], [-2, 1], [-3, -4], 3),
        ([0, 0], [0, 0], [0, 0], [0, 0], 2 ** 4),
    ],
)
def test_check_sum_of_four(
    a: List[int], b: List[int], c: List[int], d: List[int], expected_result: int
):
    actual_result = check_sum_of_four(a, b, c, d)
    assert actual_result == expected_result
