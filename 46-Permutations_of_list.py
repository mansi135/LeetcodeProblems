#Given a collection of distinct numbers, return all possible permutations.



class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) == 1:
            return [nums]

        perms = []

        for i in range(len(nums)):
            extra = nums[:i] + nums[i + 1:]
            result = self.permute(extra)
            for r in result:
                perms.append([nums[i]] + r)

        return perms