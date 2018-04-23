# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def inorderTraversal_iterative(self, root):

        stack = []
        arr = []

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                s = stack.pop()
                arr.append(s.val)
                root = s.right

        return arr

    def inorderTraversal_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        arr = []

        def helper(root):
            if root.left:
                helper(root.left)
            arr.append(root.val)
            if root.right:
                helper(root.right)

        helper(root)

        return arr


