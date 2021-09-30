def naive(string: str) -> str:
    map = {}
    for char in string:
        count = map.get(char, 0)
        if count >= 1:
            return char
        else:
            map[char] = 1
    return None


def get_recurring_char(string: str) -> str:
    """assuming string only contains lowercase letters"""
    checker = 0
    for char in string:
        bin_idx = ord(char) - ord("a")

        # will return a non-zero binary number
        # if faces the duplicate character
        if (checker & (1 << bin_idx)) > 0:
            return char

        checker = checker | (1 << bin_idx)

    return None


if __name__ == "__main__":
    testcases = [("acbbac", "b"), ("abcdef", None)]
    for (testcase, expected) in testcases:
        assert get_recurring_char(testcase) == expected
