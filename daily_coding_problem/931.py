from typing import List


def get_gcd(arr: List[int]) -> int:
    def gcd(a, b):
        while b: 
            a, b = b, a % b
        return a

    a = arr[0]
    for b in arr[1:]:
        a = gcd(a, b)

    return a


if __name__ == "__main__":
    assert get_gcd([42, 56, 14]) == 14
    assert get_gcd([2, 4, 6, 8]) == 2
