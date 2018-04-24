class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # we can find largest 3 numbers
        # neagtive two number
        # max(product of negative two and highest positive, product of highest three numbers)

        f = 0
        s = 0
        t = 0

        min1 = 0
        min2 = 0

        #O(n)
        for n in nums:
            if n > f or f == 0:
                t = s
                s = f
                f = n
            elif n > s or s == 0:
                t = s
                s = n
            elif n > t or t == 0:
                t = n

        #O(n)
        for n in nums:
            if n < min1 or min1 == 0:
                min2 = min1
                min1 = n
            elif n < min2 or min2 == 0:
                min2 = n

        #O(n)
        return max((min1 * min2 * f), (f * s * t))


#       nlogn
#         nums.sort()
#         return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

#        nlogk
#     def maximumProduct(self, nums):
#         a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)  nlogk or numslogn
#         return max(a[0] * a[1] * a[2], b[0] * b[1] * a[0])
