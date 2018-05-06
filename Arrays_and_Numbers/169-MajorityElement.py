"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Method1 - 2n
        my_dict = {}

        for n in nums:
            my_dict[n] = my_dict.get(n, 0) + 1

        for n in my_dict:
            if my_dict[n] > int(len(nums) / 2):
                return n

        # Method2 - nlogn
        # nums.sort()
        # return nums[len(nums) // 2]