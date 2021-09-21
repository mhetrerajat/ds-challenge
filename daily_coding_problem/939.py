from typing import List


def print_matrix(matrix: List[List[int]]) -> List[str]:
    rows = len(matrix)
    cols = len(matrix[0])

    top, bottom = 0, rows
    left, right = 0, cols

    print_order = []

    while top < bottom and left < right:
        # left -> right
        for idx in range(left, right):
            item = matrix[top][idx]
            print_order.append(item)
        top = top + 1

        # top -> bottom
        for idx in range(top, bottom):
            item = matrix[idx][right - 1]
            print_order.append(item)
        right = right - 1

        # right -> left
        if top < bottom:
            for idx in range(right, left, -1):
                idx = idx - 1
                item = matrix[bottom - 1][idx]
                print_order.append(item)
            bottom = bottom - 1

        # bottom -> top
        if left < right:
            for idx in range(bottom, top, -1):
                idx = idx - 1
                item = matrix[idx][left]
                print_order.append(item)
            left = left + 1

    return print_order


if __name__ == "__main__":

    matrix = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]
    print_order = print_matrix(matrix)
    assert print_order == [
        1,
        2,
        3,
        4,
        5,
        10,
        15,
        20,
        25,
        24,
        23,
        22,
        21,
        16,
        11,
        6,
        7,
        8,
        9,
        14,
        19,
        18,
        17,
        12,
        13,
    ]

    # Test Case 2
    matrix = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
    ]
    print_order = print_matrix(matrix)
    assert print_order == [
        1,
        2,
        3,
        4,
        5,
        10,
        15,
        20,
        19,
        18,
        17,
        16,
        11,
        6,
        7,
        8,
        9,
        14,
        13,
        12,
    ]

    # Test Case 3
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    assert print_matrix(matrix) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
