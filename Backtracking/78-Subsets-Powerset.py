class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        n = len(nums)
        subsets = 1 << n  # same as 2 ** n

        power_set = []

        for s in range(subsets):
            subset = []
            for i in range(n):
                mask = 1 << i
                if s & mask == mask:
                    subset.append(nums[i])

            power_set.append(subset)

        return power_set