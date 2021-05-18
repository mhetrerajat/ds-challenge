"""
This problem was asked by Google.

Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.<Paste>
"""


def get_num(arr):
    # number appeared at least once
    ones = 0
    # at least twice
    twos = 0

    for x in arr:
        twos |= ones & x
        ones ^= x

        not_three = ~(ones & twos)
        ones &= not_three
        twos &= not_three

    return ones

if __name__ == "__main__":
   assert get_num([6,1,3,3,3,6,6]) == 1
   assert get_num([13,19,13,13]) == 19
