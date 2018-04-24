# Given a string, find the first non-repeating character in it and return it's index.
# If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.


import collections


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Method-1 O(n)
        #         dictn = collections.OrderedDict()

        #         for i,c in enumerate(s):
        #             if c in dictn:
        #                 dictn[c][0] += 1
        #             else:
        #                 dictn[c] = [1, i]

        #         for v in dictn.values():
        #             if v[0] == 1:
        #                 return v[1]

        #         return -1

        # Method-2 n^2 ?
        #         indices = []
        #         for i,c in enumerate(s):
        #             if s.count(c) == 1:
        #                 return i

        #         return -1

        # Method-3 O(n) because 26 letters is a constant
        # letters = [chr(x) for x in range(ord('a'), ord('z')+1)]

        letters = 'abcdefghijklmnopqrstuvwxyz'

        index = [s.index(l) for l in letters if s.count(l) == 1]

        return min(index) if len(index) > 0 else -1