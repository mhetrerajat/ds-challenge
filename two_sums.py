# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for item_index, item in enumerate(nums):
            nums[item_index] = 'TEMPORARY_REPLACEMENT'
            ideal_value = target-item
            if ideal_value in nums:
                # found that number
                # return its index
                another_item_index = nums.index(ideal_value)
                return [item_index, another_item_index]
            nums[item_index] = item
                
        return []