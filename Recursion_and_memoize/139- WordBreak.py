"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""

class Solution(object):

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict.sort(key=lambda x: len(x))
        self.memo = {}
        return self.canSegment(s, wordDict)

    def canSegment(self, s, wordDict):
        if len(s) == 0:
            return True
        if s in self.memo:
            return self.memo[s]
        for word in wordDict:
            if len(word) > len(s):
                break
            if word == s[:len(word)] and self.canSegment(s[len(word):], wordDict):
                return True
        self.memo[s] = False
        return False


## Time Limit exceeded for the following method :

#     def wordBreak(self, s, wordDict):
#         """
#         :type s: str
#         :type wordDict: List[str]
#         :rtype: bool
#         """

#         wordDict = set(wordDict)
#         self.cache = {}
#         return self.memoized(s, 0, wordDict)


#     def helper(self, s, start, wordDict):

#         if start == len(s):
#             return True

#         for i in range(start, len(s)):
#             if s[start:i+1] in wordDict and self.memoized(s, i+1, wordDict):
#                 return True

#       #  self.cache[s] = False
#         return False

#     def memoized(self, s, start, wordDict):

#         r = self.cache.get(start)

#         if not r:
#             r = self.helper(s, start, wordDict)
#             self.cache[start] = r

#         return r 