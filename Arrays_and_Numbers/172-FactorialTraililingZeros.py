class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n >= 5:
            return n / 5 + self.trailingZeroes(n / 5)
        else:
            return 0