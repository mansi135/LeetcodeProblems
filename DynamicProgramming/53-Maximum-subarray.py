class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # this is slightly modified version of Kadane's algorithm
        if not nums:
            return []

        max_so_far = nums[0]
        current_max = nums[0]

        for i in range(1, len(nums)):
            current_max = max(nums[i], current_max + nums[i])
            max_so_far = max(max_so_far, current_max)

        return max_so_far