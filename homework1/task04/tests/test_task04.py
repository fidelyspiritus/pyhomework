from typing import List

import pytest

from homework1.task04 import check_sum_of_four


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (([1, 2], [1, 2], [-2, 1], [-3, -4]), 2),
        (([0, 0], [0, 0], [0, 0], [0, 0]), 2 ** 4),
    ],
)
def test_check_sum_of_four(
    value: (List[int], List[int], List[int], List[int]), expected_result: int
):
    actual_result = check_sum_of_four(value)
    assert actual_result == expected_result
