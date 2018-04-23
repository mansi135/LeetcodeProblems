# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def preorderTraversal_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        output = [root.val]

        if root.left:
            output += self.preorderTraversal(root.left)

        if root.right:
            output += self.preorderTraversal(root.right)

        return output

    def preorderTraversal(self, root):

        # if not root:
        #     return []

        stack = [root]
        values = []
        # i = 0

        while len(stack) > 0:
            current = stack.pop()
            if current:
                values.append(current.val)
                stack.append(current.right)
                stack.append(current.left)

        return values

