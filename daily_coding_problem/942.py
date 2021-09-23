def get_num_paranthesis_required(string: str) -> int:
    stack = []
    for item in string:
        poped_item = stack.pop() if stack else None
        if poped_item == "(" and item == ")":
            pass
        else:
            if poped_item:
                stack.append(poped_item)
            stack.append(item)

    return len(stack)


if __name__ == "__main__":
    test_cases = [("()())()", 1), (")(", 2), ("", 0), ("())", 1), ("(((", 3)]
    for (testcase, expectd_output) in test_cases:
        assert get_num_paranthesis_required(testcase) == expectd_output
