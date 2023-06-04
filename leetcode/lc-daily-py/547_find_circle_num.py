# https://leetcode.com/problems/number-of-provinces/
# 547. Number of Provinces


from typing import List


def findCircleNum(isConnected: List[List[int]]) -> int:
    cities = len(isConnected)
    visited = [0] * cities

    result = 0
    for vtx in range(cities):
        if not visited[vtx]:
            result += 1

            stack = [vtx]
            visited[vtx] = 1
            while stack:
                cur = stack.pop()
                for v, nbr in enumerate(isConnected[cur]):
                    if v != cur and nbr == 1 and not visited[v]:
                        visited[v] = 1
                        stack.append(v)

    return result


assert findCircleNum([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]) == 1
assert findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
assert findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3
