"""
This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""

from functools import lru_cache


@lru_cache(maxsize=None)
def _fixed_choices(n):
    if n == 0 or n == 1:
        return 1
    else:
        return _fixed_choices(n-1) + _fixed_choices(n-2)

@lru_cache(maxsize=None)
def _combinations(n, choices):
    if n == 0:
        return 1
    else:
        _count = 0
        for i in choices:
            if n-i >= 0:
                _count += _combinations(n-i, choices)

        return _count


def get_unique_ways(n, choices):
    ways = _combinations(n, choices)
    return ways



if __name__ == "__main__":
    assert get_unique_ways(4, (1,2)) == 5
    for (n, choices) in [(10, (1,2)), (20, (1,3,5)), (50, (1,2,3)), (100, (1,3))]:
        print(n, choices, get_unique_ways(n, choices), _combinations.cache_info())

