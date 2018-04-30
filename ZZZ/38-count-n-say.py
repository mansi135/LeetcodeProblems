class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        if n == 1:
            return '1'
        elif n == 2:
            return '11'

        n_str = '11'

        for _ in range(3, n + 1):
            tmp_str = ""
            count = 1
            for c in range(1, len(n_str)):
                if n_str[c] != n_str[c - 1]:
                    tmp_str += str(count) + n_str[c - 1]
                    count = 1
                else:
                    count += 1
            tmp_str += str(count) + n_str[-1]
            n_str = tmp_str

        return n_str


