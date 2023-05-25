# https://leetcode.com/problems/maximum-subsequence-score/description/
# 2542. Maximum Subsequence Score
# LC Daily - 24/05/2023

from typing import List

def max_score(nums1: List[int], nums2: List[int], k:int) -> int:
	n = len(nums1)

	# sort in desc order of nums2
	srt_nums = sorted([(n2, n1) for n2, n1 in zip(nums2, nums1)], reverse=True)

	# maintain minheap
	from heapq import heappop, heappush
	mh = []
	_sum, _ans = 0, 0
	for (n2, n1) in srt_nums:
		heappush(mh, n1)
		_sum += n1
		if len(mh) > k:
			popnum = heappop(mh)
			_sum -= popnum
		elif len(mh) == k:
			_ans = max(_ans, _sum * n2)

	return _ans
	


testcases = [
	([1,3,3,2], [2,1,3,4], 3, 12),
	([4,2,3,1,1], [7,5,10, 9,6], 1, 30)
]
for (nums1, nums2, k, expected) in testcases:
	assert max_score(nums1, nums2, k) == expected