def get_possible_ways(n: int) -> int:
    """Tile can either be placed horizontally or vertically"""
    memo = [0] * (n+1)
    memo[0] = 0
    memo[1] = 1

    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]

    return memo[-1]


if __name__ == "__main__":
    testcases = [(4, 3), (3, 2), (2, 1), (1, 1)]
    for (testcase, expected_output) in testcases:
        assert get_possible_ways(testcase) == expected_output
