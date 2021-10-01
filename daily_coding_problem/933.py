from typing import List


def get_arr(sign_arr: List[str]) -> List[int]:
    result = []
    max_num = 0
    for idx, sign in enumerate(sign_arr):
        if sign is None:
            result.append(0)
        elif sign == "+":
            num = max_num + 1
            result.append(num)
            max_num = num
        elif sign == "-":
            # "-" sign
            # Add 1 to all other numbers
            for ridx, rnum in enumerate(result):
                result[ridx] = rnum + 1
            max_num = max_num + 1

            # Add zero for - sign
            result.append(0)

    return result


if __name__ == "__main__":
    testcases = [
        ([None, "+", "+", "-", "+"], [1, 2, 3, 0, 4]),
        ([None, "+", "+", "+", "+", "+"], [0, 1, 2, 3, 4, 5]),
        ([None, "-", "-", "-"], [3, 2, 1, 0]),
        ([None, "-", "+"], [1, 0, 2]),
        ([None, "+", "-", "+", "-"], [2, 3, 1, 4, 0]),
    ]
    for (testcase, expected) in testcases:
        assert get_arr(testcase) == expected
