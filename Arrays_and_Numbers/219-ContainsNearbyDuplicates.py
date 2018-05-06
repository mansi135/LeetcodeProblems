from collections import defaultdict


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        my_dict = defaultdict(list)

        for i in range(len(nums)):
            if nums[i] in my_dict:
                for j in my_dict[nums[i]]:
                    if abs(j - i) <= k:
                        return True

            my_dict[nums[i]].append(i)

        return False


from collections import defaultdict


# Alternate method
class Solution(object):
    def alter(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        my_dict = {}

        for i in range(len(nums)):
            if nums[i] in my_dict and abs(i - my_dict[nums[i]]) <= k:
                return True
            my_dict[nums[i]] = i

        return False
