def get_possible_ways(n: int) -> int:
    """Tile can either be placed horizontally or vertically"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return get_possible_ways(n - 1) + get_possible_ways(n - 2)


if __name__ == "__main__":
    testcases = [(4, 3), (3, 2), (2, 1), (1, 1)]
    for (testcase, expected_output) in testcases:
        print(get_possible_ways(testcase))
        assert get_possible_ways(testcase) == expected_output
