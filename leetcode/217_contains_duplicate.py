# https://leetcode.com/problems/contains-duplicate/
# Neetcode - Arrays & Hashing

from typing import List

def contains_dups(nums: List[int]) -> bool:
	hm = set()
	for n in nums:
		if n not in hm:
			hm.add(n)
		else:
			return True
	return False		

testcases = [
	([1,2,3,1], True),
	([1,2,3,4], False),
	([1,1,1,3,3,4,3,2,4,2], True)
]

for (nums, expected) in testcases:
	contains_dups(nums) == expected
