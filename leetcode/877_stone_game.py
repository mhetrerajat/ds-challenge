# https://leetcode.com/problems/stone-game/
# 877. Stone Game

from typing import List
from functools import lru_cache


def stoneGame(piles: List[int]) -> bool:
    dp = {}

    # compute max alice can score
    @lru_cache(None)
    def dpf(l, r):
        # nothing left to choose from
        if l > r:
            return 0

        if (l, r) in dp:
            return dp[(l, r)]

        # whose turn to choose from the piles
        is_even = (r - l) % 2 != 0

        left = piles[l] if is_even else 0
        right = piles[r] if is_even else 0

        dp[(l, r)] = max(dpf(l+1, r) + left, dpf(l, r-1) + right)

        return dp[(l, r)]
        

    length = len(piles)
    return dpf(0, length - 1) > 0


assert stoneGame([5, 3, 4, 5]) == True
assert stoneGame([3, 7, 2, 3]) == True
