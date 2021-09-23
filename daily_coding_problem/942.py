def space_efficient(string: str) -> int:
    balance = 0
    added = 0
    for item in string:
        if item == "(":
            balance += 1
        else:
            balance -= 1

        if balance == -1:
            balance += 1
            added += 1

    return added + balance


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
    test_cases = [
        ("()())()", 1),
        (")(", 2),
        ("", 0),
        ("())", 1),
        ("(((", 3),
        (")))", 3),
    ]
    for (testcase, expectd_output) in test_cases:
        assert space_efficient(testcase) == expectd_output
