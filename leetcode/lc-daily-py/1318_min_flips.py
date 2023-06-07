# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/
# 1318. Minimum Flips to Make a OR b Equal to c


from typing import Callable


def minFlips(a: int, b: int, c: int) -> int:
    result = 0

    while a or b or c:
        if c & 1 == 1:
            result += 0 if (a & 1) or (b & 1) else 1
        else:
            result += (a & 1) + (b & 1)

        a >>= 1
        b >>= 1
        c >>= 1

    return result


# 0010 | 0110 == 0101
assert minFlips(2, 6, 5) == 3

# 0100 | 0010 == 0111
assert minFlips(4, 2, 7) == 1

# 0001 | 0010 == 0011
assert minFlips(1, 2, 3) == 0

# 0111 | 0011 == 0111
assert minFlips(7, 3, 7) == 0

# 0001 | 0001 == 0000
assert minFlips(1, 1, 0) == 2
