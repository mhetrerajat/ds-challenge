import sys
from typing import List, Tuple


def get_propagation_time(vertices: int, edges: List[Tuple[int]]) -> int:
    """Compute total time to send message from start to end node"""

    # Find the shortest time required to visit each node from source
    # The propation time is equal to maximum of time to visit each node from source

    graph = {idx: [] for idx in range(vertices + 1)}
    for (u, v, w) in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    times = [sys.maxsize] * (vertices + 1)
    times[0] = 0
    processed = [False] * (vertices + 1)

    for _ in range(vertices + 1):

        # Find the node with min times which is not processed
        processing_node = None
        min_weight = sys.maxsize
        for idx, _time in enumerate(times):
            if not processed[idx] and min_weight > _time:
                min_weight = _time
                processing_node = idx

        # Re-calculate time for adjacent nodes
        neighbours = graph[processing_node]
        for (neighbour, weight) in neighbours:
            if not processed[neighbour]:
                new_weight = times[processing_node] + weight
                if times[neighbour] > new_weight:
                    times[neighbour] = new_weight

        # Mark node as processed
        processed[processing_node] = True

    propagation_time = max(times)

    return propagation_time


if __name__ == "__main__":
    N = 5
    edges = [
        (0, 1, 5),
        (0, 2, 3),
        (0, 5, 4),
        (1, 3, 8),
        (2, 3, 1),
        (3, 5, 10),
        (3, 4, 5),
    ]
    propagation_time = get_propagation_time(vertices=N, edges=edges)
    assert propagation_time == 9
