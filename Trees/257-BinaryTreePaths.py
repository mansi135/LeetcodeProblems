"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        if not root:
            return []

        paths = []

        def helper(root, s):

            s += str(root.val)

            if root.left is None and root.right is None:
                paths.append(s)
                return

            s += '->'

            if root.left:
                helper(root.left, s)

            if root.right:
                helper(root.right, s)

        helper(root, '')

        return paths



