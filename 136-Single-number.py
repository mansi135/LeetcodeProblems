# Given an array of integers, every element appears twice except for one. Find that single one.

#Note:
#Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        i = 0
        while i < len(nums) - 2:
            if nums[i] == nums[i + 1]:
                i += 2
            else:
                return nums[i]

        return nums[-1]

    def alter(self, nums):
        res = 0

        for n in nums:
            res = res ^ n  #xor

        return res