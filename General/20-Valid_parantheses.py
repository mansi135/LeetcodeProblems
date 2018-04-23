#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        dict_brackets = {'(': ')', '{': '}', '[': ']'}

        for char in s:
            if char in dict_brackets:
                stack.append(char)
            elif char in dict_brackets.values(): # O(n^2) ; if we make a set of dict.values(), it could be made O(n)
                if not stack or dict_brackets.get(stack.pop()) != char:
                    return False

        return len(stack) == 0

