# https://leetcode.com/problems/two-sum/
# 1. Two Sum
# Neetcode - 3


from collections import defaultdict
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    hm = defaultdict(int)
    for idx, n in enumerate(nums):
        if n in hm:
            return [hm[n], idx]
        m = target - n
        hm[m] = idx

    # solution don't exists, but this won't happen as per problem definition
    return [-1, -1]


assert twoSum([2, 7, 11, 15], 9) == [0, 1]
assert twoSum([3, 2, 4], 6) == [1, 2]
assert twoSum([3, 3], 6) == [0, 1]  # duplicate numbers
assert twoSum([-3, -4, 7, -1, 2], 1) == [3, 4]  # negative numbers
assert twoSum([1000000000, 20000000, -1000000000, 30000000], 0) == [0, 2]
