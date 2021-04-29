"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    max_sum = 0
    for first in range(len(nums)):
        for last in range(first, first + k + 1):
            if last > len(nums):
                break
            if sum((nums[first:last])) > max_sum:
                max_sum = sum((nums[first:last]))

    return max_sum
