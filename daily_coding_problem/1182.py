"""
This problem was asked by Etsy.

Given an array of numbers N and an integer k, 
your task is to split N into k partitions such that 
the maximum sum of any partition is minimized. Return this sum.

For example, given N = [5, 1, 2, 7, 3, 4] and k = 3, 
you should return 8, since the optimal partition is [5, 1, 2], [7], [3, 4].
"""


def main(N, k):
    min_sum = max(N)
    max_sum = sum(N)

    left, right = min_sum, max_sum

    while left < right:
        mid = (left + right) >> 1
        if check_partition(N, mid, k):
            right = mid
        else:
            left = mid + 1
    return left


def check_partition(N, target, k):
    _sum = 0
    n_partitions = 1

    for x in N:
        if _sum + x > target:
            _sum = x
            n_partitions += 1

            if n_partitions > k:
                return False
        else:
            _sum += x

    return True


if __name__ == "__main__":
    N = [5, 1, 2, 7, 3, 4]
    k = 3
    assert main(N, k) == 8
