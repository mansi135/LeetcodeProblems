"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


# This is binary solution using bit masking
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


# This method is called backtracking -> take self and dont take self (to build a tree)
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        output = []

        def helper(i, curr):
            if i == len(nums):
                output.append(curr)
                return

            # take self
            withself = curr[:]
            withself.append(nums[i])
            helper(i + 1, withself)

            # dont take self
            helper(i + 1, curr)

        helper(0, [])

        return output


