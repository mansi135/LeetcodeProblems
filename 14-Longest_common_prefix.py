#Write a function to find the longest common prefix string amongst an array of strings.
#Time Complexity - O(n^2)

import unittest

class Solution:

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        longest_prefix = ''
        s = ''
        
        for letter in strs[0]:
            s += letter
            for word in strs[1:]:
                if not word.startswith(s):
                    return longest_prefix
            longest_prefix = s
            
        return longest_prefix


    def alternate_solution(self, strs):

        if not strs:
            return ""

        min_word = min(strs, key = len) # if we dont use min length word, then we get a index error

        for i, letter in enumerate(min_word):
            ch = min_word[i]
            for word in strs:
                if word[i] != ch:
                    return min_word[:i]

        return min_word



class MyTestCases(unittest.TestCase):

  def test_longest(self):

      my_object = Solution()
      self.assertEqual(my_object.longestCommonPrefix(['magicball', 'mag', 'maggie']), 'mag')

  def test_alternate(self):

      my_object = Solution()
      self.assertEqual(my_object.alternate_solution(['magicball', 'mag', 'maggie']), 'mag')


if __name__ == "__main__":

    unittest.main()