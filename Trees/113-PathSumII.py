"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.all_paths = []
        one_path = []

        self.dfs(root, sum, one_path)

        return self.all_paths

    def dfs(self, root, sum, one_path):

        if not root:
            return

        one_path.append(root.val)

        if root.left is None and root.right is None and root.val == sum:
            path = one_path[:]
            self.all_paths.append(path)

        self.dfs(root.left, sum - root.val, one_path)

        self.dfs(root.right, sum - root.val, one_path)

        one_path.pop()

