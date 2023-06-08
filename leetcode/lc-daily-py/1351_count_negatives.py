# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
# 1351. Count Negative Numbers in a Sorted Matrix


from typing import List


def countNegatives(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    count = 0
    for i in range(m):
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            x = grid[i][mid]
            if x >= 0:
                left = mid + 1
            elif x < 0:
                right = mid - 1

        count += n - left
    return count


def naive(grid):
    m, n = len(grid), len(grid[0])
    count = 0
    for i in range(m):
        for j in range(n):
            x = grid[i][j]
            if x < 0:
                count += 1
    return count


assert (
    countNegatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]])
    == 8
)
assert countNegatives([[3, 2], [1, 0]]) == 0
