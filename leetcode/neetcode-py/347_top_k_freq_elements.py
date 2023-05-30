# https://leetcode.com/problems/top-k-frequent-elements/
# 347. Top K Frequent Elements
# NeetCode - 5


from collections import Counter, defaultdict
from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    # return naive(nums, k)

    # QuickSelect
    hm = Counter(nums)

    arr = list(hm.keys())

    def partition(left: int, right: int, pvtidx: int) -> int:
        # move pivot to end
        pfreq = hm[arr[pvtidx]]
        arr[pvtidx], arr[right] = arr[right], arr[pvtidx]

        i = left
        for j in range(left, right):
            if hm[arr[j]] < pfreq:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[right], arr[i] = arr[i], arr[right]

        return i

    def quickselect(left: int, right: int, k_smallest: int) -> None:
        import random

        if left == right:
            return

        pvtidx = random.randint(left, right)
        pvtidx = partition(left, right, pvtidx)

        if k_smallest < pvtidx:
            quickselect(left, pvtidx - 1, k_smallest)
        elif k_smallest > pvtidx:
            quickselect(pvtidx + 1, right, k_smallest)
        else:
            # k_smallest == pvtidx
            return

    n = len(arr)
    quickselect(0, n - 1, n - k)

    return arr[n - k :]


# DEPRECATED
def naive(nums, k):
    hm = defaultdict(int)
    for x in nums:
        hm[x] += 1

    sorted_nums = sorted(
        [(n, c) for n, c in hm.items()], key=lambda x: x[-1], reverse=True
    )

    return [x for x, _ in sorted_nums[:k]]


assert sorted(topKFrequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
assert sorted(topKFrequent([1], 1)) == [1]
