class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        a = list(str(x))[::-1]

        if x < 0:
            a.pop()

        b = int("".join(a))

        if x < 0:
            if b > 2147483648:
                return 0
            else:
                return -b

        elif x >= 0:

            if b > 2147483647:
                return 0
            else:
                return b
