# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # this is not min height
        if not root:
            return 0

        if root.left is None and root.right is None:
            return 1

        l = 0
        r = 0

        if root.left:
            l = l + self.minDepth(root.left)

        if root.right:
            r = r + self.minDepth(root.right)

        # print(l,r)
        if l == 0:
            return r + 1

        elif r == 0:
            return l + 1

        else:
            return min(l, r) + 1

    def minDepth_altr(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # this is not min height

        if not root:
            return 0

        l = self.minDepth(root.left)
        r = self.minDepth(root.right)

        if l == 0 or r == 0:
            return l + r + 1

        else:
            return min(l, r) + 1
