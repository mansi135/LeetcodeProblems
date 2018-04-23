class Solution(object):
    memoized_result = {}

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        # memoize it like fibonacci, otherise following will give 'Time limit exceeded'

        #         if n == 1:
        #             return 1

        #         elif n == 2:
        #             return 2

        #         else:
        #             return self.climbStairs(n-1) + self.climbStairs(n-2)

        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            if (n - 1) in self.memoized_result:
                first = self.memoized_result[n - 1]
            else:
                first = self.climbStairs(n - 1)
                self.memoized_result[n - 1] = first

            if (n - 2) in self.memoized_result:
                second = self.memoized_result[n - 2]
            else:
                second = self.climbStairs(n - 2)
                self.memoized_result[n - 2] = second

            return first + second

