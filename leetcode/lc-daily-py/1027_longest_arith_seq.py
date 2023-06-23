# https://leetcode.com/problems/longest-arithmetic-subsequence/
# 1027. Longest Arithmetic Subsequence


from types import ClassMethodDescriptorType
from typing import List
from collections import defaultdict


def longestArithSeqLength(nums: List[int]) -> int:
    result = 2
    length = len(nums)

    dp = defaultdict(dict)

    for left in range(length):
        for right in range(left + 1, length):
            diff = nums[right] - nums[left]
            dp[(right, diff)] = dp.get((left, diff), 1) + 1
            result = max(result, dp[(right, diff)])
    return result


def naive(nums: List[int]) -> int:
    result = 0
    length = len(nums)

    def compute_len(nums, start, diff):
        count = 1
        prev = nums[start]
        for x in range(start + 1, len(nums)):
            if (nums[x] - prev) == diff:
                prev = nums[x]
                count += 1
        return count

    for left in range(length):
        for right in range(left + 1, length):
            diff = nums[right] - nums[left]
            _length = 1 + compute_len(nums, right, diff)
            result = max(result, _length)

    return result


assert longestArithSeqLength([3, 6, 9, 12]) == 4
assert longestArithSeqLength([9, 4, 7, 2, 10]) == 3
assert longestArithSeqLength([20, 1, 15, 3, 10, 5, 8]) == 4
