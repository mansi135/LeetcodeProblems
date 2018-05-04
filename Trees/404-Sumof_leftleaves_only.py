"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        s = self.helper(root)

        return s

    def helper(self, root):

        sum_left = 0

        if root.left:
            if root.left.left is None and root.left.right is None:
                sum_left += root.left.val
            else:
                sum_left += self.helper(root.left)

        if root.right:
            sum_left += self.helper(root.right)

        return sum_left



# Method-2
    def combined_in_one(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        sum_left = 0

        if root.left:
            if root.left.left is None and root.left.right is None:
                sum_left += root.left.val
            else:
                sum_left += self.sumOfLeftLeaves(root.left)

        if root.right:
            sum_left += self.sumOfLeftLeaves(root.right)

        return sum_left