class Solution:
    def isPalindrome_al(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if not s:
            return True

        l = 0
        r = len(s) - 1

        # O(n)
        while l < r:
            # print(s[l], s[r])
            while not s[l].isalnum() and l < r:
                l += 1
            while not s[r].isalnum() and r > l:
                r -= 1
            if s[l].lower() != s[r].lower():
                print(s[l], s[r])
                return False
            l += 1
            r -= 1

        return True

    def isPalindrome(self, s):

        if not s:
            return True

        # O(n)
        s_modified = [c.lower() for c in s if c.isalnum()]

        # O(n) + S(n) since slicing creates a copy of new list
        return s_modified == s_modified[::-1]