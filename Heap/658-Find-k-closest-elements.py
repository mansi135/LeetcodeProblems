# Given a sorted array, two integers k and x, find the k closest elements to x in the array.
#  The result should also be sorted in ascending order.
# If there is a tie, the smaller elements are always preferred.
#
# Example 1:
# Input: [1,2,3,4,5], k=4, x=3
# Output: [1,2,3,4]
# Example 2:
# Input: [1,2,3,4,5], k=4, x=-1
# Output: [1,2,3,4]

import heapq
from operator import itemgetter

class Solution(object):

    # Without using heap , simple sort - nlogn
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        res = []

        # O(n)
        for n in arr:
            res.append((n, abs(n - x)))

        # O(nlogn)
        res.sort(key=lambda x: x[1])

        # O(n)
        final = [res[i][0] for i in range(k)]

        # O(nlogn)
        final.sort()

        return final

    # Using heap - still nlogn
    def alter(self, arr, k, x):

        res = []

        # O(n)
        for n in arr:
            res.append((n, abs(n - x)))

        # O(klogk) - then there is no need to sort
        final = heapq.nsmallest(k, res, key=itemgetter(1))

        # O(n)
        final = [x[0] for x in final]
        # print(final)

        # O(nlogn)
        final.sort()

        return final


    # using binary search and two - pointer