# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        if root.left is None and root.right is None:
            return 1

        left_ht = 0
        right_ht = 0

        if root.left:
            left_ht = 1 + self.maxDepth(root.left)

        if root.right:
            right_ht = 1 + self.maxDepth(root.right)

        return max(left_ht, right_ht)
