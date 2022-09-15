"""
This problem was asked by Microsoft.

Given an array of numbers and a number k, determine if there are three entries in the array which add up to the specified number k. For example, given [20, 303, 3, 4, 25] and k = 49, return true as 20 + 4 + 25 = 49.
"""

def two_sum(A, t, dups):
    _map = {}

    for n in A:
        if n in dups:
            continue
        at = t - n
        if at in _map.keys():
            return [at, n]
        else:
            _map[n] = at
    return None

def check_k(A, k):
    _map = {}

    for ix, i in enumerate(A):
        dups = set([i])
        t = k - i
        _r = two_sum(A, t, dups)
        if _r:
            r = sorted([i] + _r)
            return tuple(r)

    


if __name__ == "__main__":
    A = [20, 303, 3, 4, 25]
    k = 49
    assert check_k(A, k) == (4, 20, 25)
