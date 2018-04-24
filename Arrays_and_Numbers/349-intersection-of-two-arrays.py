class Solution(object):

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        return list(set(nums1) & set(nums2))

    def intersection_alter(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) != len(nums2):
            shortest = min(nums1, nums2, key=len)
            longest = max(nums1, nums2, key=len)
        else:
            shortest = nums1
            longest = nums2

        intersection = set()
        longest = set(longest)

        for n in shortest:
            if n in longest:
                intersection.add(n)

        return list(intersection)

