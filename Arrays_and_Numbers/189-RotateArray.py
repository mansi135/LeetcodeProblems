# Given an array, rotate the array to the right by k steps, where k is non-negative.
#
# Example 1:
#
# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:
#
# Input: [-1,-100,3,99] and k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
# Note:
#
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
# Could you do it in-place with O(1) extra space?


class Solution(object):

    # Method-1 O(n) time, O(n) space
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        k = k % n
        new_array = [0] * n

        i = n - 1

        while i >= 0:
            new_array[(i + k) % n] = nums[i]
            i -= 1

        nums[:] = new_array[:]

        # One-liner-method-2 -> O(n) time , O(n) space
        # nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]

        # Method-3 Rotate one by one: O(1) space, but O(n*k) time

        # Method-4 GCD Juggling Algorithm


    #Method-5 reverse
    # In this method , we reverse the half of lists first and then reverse the entire list
    # O(n) time and O(1) space

    def reverse(self, nums, l, r):

        while l < r:
            tmp = nums[l]
            nums[l] = nums[r]
            nums[r] = tmp
            l += 1
            r -= 1

    def rotate_alternate(self, nums, k):

        n = len(nums)
        k = k % n

        self.reverse(nums, 0, n - k - 1) #O(n) time
        self.reverse(nums, n - k, n - 1) #O(n) time

        self.reverse(nums, 0, n - 1) #O(n) time