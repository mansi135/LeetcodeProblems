class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False

        # to find number of digits

        div = 1

        while int(x / div) >= 10:
            div = div * 10

        while x != 0:
            first_d = int(x / div)
            last_d = x % 10
            print(first_d, last_d)
            if first_d != last_d:
                return False

            # chop first and last digit
            x = int((x % div) / 10)
            div = div / 100

        return True