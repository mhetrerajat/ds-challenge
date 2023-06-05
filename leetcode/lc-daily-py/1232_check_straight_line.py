# https://leetcode.com/problems/check-if-it-is-a-straight-line/
# 1232. Check If It Is a Straight Line


from typing import List


def checkStraightLine(coordinates: List[List[int]]) -> bool:
    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]

    try:
        m = (y2 - y1) / (x2 - x1)
        is_on_line = lambda x: (x[1] - y2 == m * (x[0] - x2))
    except ZeroDivisionError as _:
        is_on_line = lambda x: x[0] == x2

    for idx in range(2, len(coordinates)):
        x, y = coordinates[idx]
        if not is_on_line((x, y)):
            return False

    return True


assert checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) == True

assert checkStraightLine([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]) == False

# case where slope is undefined
assert checkStraightLine([[0, 0], [0, 1], [0, -1]]) == True
