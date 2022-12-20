# https://practice.geeksforgeeks.org/problems/save-ironman/0

import math


def check_palindrome(s):
    if len(s) == 0:
        return "NO"

    l = 0
    r = len(s) - 1

    while l != r and l != len(s):

        is_valid_l = any([s[l].isalpha(), s[l].isdigit()])
        is_valid_r = any([s[r].isalpha(), s[r].isdigit()])

        if is_valid_l and is_valid_r:
            if s[l].lower() != s[r].lower():
                return "NO"

        if is_valid_l and not is_valid_r:
            r -= 1
        elif not is_valid_l and is_valid_r:
            l += 1
        else:
            l += 1
            r -= 1

    return "YES"


def main():
    T = 1
    S = ["I am :IronnorI Ma, i", "Ab?/Ba"]
    for s in S:
        print(check_palindrome(s))


if __name__ == "__main__":
    main()