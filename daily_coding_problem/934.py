def get_recurring_char(string: str) -> str:
    map = {}
    for char in string:
        count = map.get(char, 0)
        if count >= 1:
            return char
        else:
            map[char] = 1
    return None


if __name__ == "__main__":
    testcases = [("acbbac", "b"), ("abcdef", None)]
    for (testcase, expected) in testcases:
        assert get_recurring_char(testcase) == expected
