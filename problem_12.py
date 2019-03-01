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

