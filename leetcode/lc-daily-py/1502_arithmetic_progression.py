# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
# 1502. Can Make Arithmetic Progression From Sequence


from typing import List


def canMakeArithmeticProgression(arr: List[int]) -> bool:
    _max, _min = max(arr), min(arr)

    n = len(arr)
    if (_max - _min) == 0:
        return True
    elif (_max - _min) % (n - 1) != 0:
        return False
    else:
        diff = (_max - _min) // (n - 1)

    uarr = set()
    for x in arr:
        if (x - _min) % diff != 0:
            return False
        else:
            uarr.add(x)

    return len(uarr) == n


def naive(arr):
    left = 1
    right = len(arr) - 1

    arr = sorted(arr)

    for idx in range(left, right):
        prev = arr[idx - 1]
        curr = arr[idx]
        nxt = arr[idx + 1]

        if abs(prev - curr) != abs(curr - nxt):
            return False
    return True


assert canMakeArithmeticProgression([3, 5, 1]) == True
assert canMakeArithmeticProgression([1, 2, 4]) == False
assert canMakeArithmeticProgression([1, 2]) == True
assert canMakeArithmeticProgression([-1, 0, 1]) == True
