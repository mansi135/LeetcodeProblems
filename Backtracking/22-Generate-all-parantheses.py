"""

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

# no need to pass 'n' in helper -- can be removed
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def helper(s, op, cl, n):
            if op == n and cl == n:
                res.append(s)
            else:
                if op < n:
                    helper(s + '(', op + 1, cl, n)
                if cl < op:
                    helper(s + ')', op, cl + 1, n)

        helper("", 0, 0, n)

        return res

