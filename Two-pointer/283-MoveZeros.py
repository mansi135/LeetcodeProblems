class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        ptr1 = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                tmp = nums[ptr1]
                nums[ptr1] = nums[i]
                nums[i] = tmp
                ptr1 += 1
