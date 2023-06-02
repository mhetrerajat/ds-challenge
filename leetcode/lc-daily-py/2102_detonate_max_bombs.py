# https://leetcode.com/problems/detonate-the-maximum-bombs/
# 2101. Detonate the Maximum Bombs


from collections import defaultdict
from typing import DefaultDict, List
import math


def maximumDetonation(bombs: List[List[int]]) -> int:
    def dist(x, y, m, n):
        return math.sqrt(((x - m) ** 2) + ((y - n) ** 2))

    # build graph
    graph = defaultdict(list)
    for i, (x, y, r1) in enumerate(bombs):
        for j, (m, n, r2) in enumerate(bombs):
            if i == j:
                continue

            if dist(x, y, m, n) <= r1:
                graph[i].append(j)

    # dfs
    def dfs(x):
        stack = [x]
        visited = set([x])
        while stack:
            cur = stack.pop()
            for neigh in graph[cur]:
                if neigh not in visited:
                    visited.add(neigh)
                    stack.append(neigh)
        return len(visited)

    result = 0
    for i, _ in enumerate(bombs):
        result = max(result, dfs(i))
    return result


assert maximumDetonation([[2, 1, 3], [6, 1, 4]]) == 2
assert maximumDetonation([[1, 1, 5], [10, 10, 5]]) == 1
assert maximumDetonation([[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]) == 5
