class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # tricky solution - referred geeks for geeks
        # O(n) time and O(n) space would be to make a set and check if element in set, add to duplicates

        res = []

        for n in nums:
            if nums[abs(n) - 1] < 0:
                res.append(abs(n))
            else:
                nums[abs(n) - 1] *= -1

        return res


