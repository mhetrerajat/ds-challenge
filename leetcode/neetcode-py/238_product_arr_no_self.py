# https://leetcode.com/problems/product-of-array-except-self/
# 238. Product of Array Except Self
# Neetcode - 6

"""
NOTE 
- an algorithm that runs in O(n) time and without using the division operation.
- solve the problem in O(1) extra space complexity
"""
from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    # return naive(nums)
    # return better_but_space(nums)
    n = len(nums)
    arr = [1] * n

    # 1 2 3 4 -> L: 1 1 2 6 | R: 24 12 4 1
    # arr -> 1 1 2 6 -> 1 1 2 6
    for idx in range(1, n):
        arr[idx] = arr[idx - 1] * nums[idx - 1]

    R = 1
    for idx in reversed(range(n)):
        arr[idx] *= R
        R *= nums[idx]

    return arr


def better_but_space(nums):
    n = len(nums)
    L, R, arr = [1] * n, [1] * n, [1] * n

    L[1] = 1
    for idx in range(1, n):
        L[idx] = L[idx - 1] * nums[idx - 1]

    R[n - 1] = 1
    for idx in reversed(range(0, n - 1)):
        R[idx] = R[idx + 1] * nums[idx + 1]
    print(L, R)
    for idx in range(n):
        arr[idx] = L[idx] * R[idx]
    return arr


# FAILS
def better_but_div(nums):
    n = len(nums)
    _mul = 1
    for a in nums:
        _mul *= a

    arr = [_mul] * n

    for idx, a in enumerate(nums):
        arr[idx] /= a or 1

    return arr


def naive(nums):
    arr = []
    for i, _ in enumerate(nums):
        _mul = 1
        for j, b in enumerate(nums):
            if i != j:
                _mul *= b
        arr.append(_mul)
    return arr


assert productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
assert productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
