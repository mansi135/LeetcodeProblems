# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.is_balanced_helper(root)[1]

    def is_balanced_helper(self, root):

        if not root:
            return (0, True)

        if root.left is None and root.right is None:
            return (1, True)

        lt_ht = 1
        rt_ht = 1

        if root.left:
            left_result = self.is_balanced_helper(root.left)
            if left_result[1] == False:
                return (0, False)
            lt_ht += left_result[0]

        if root.right:
            right_result = self.is_balanced_helper(root.right)
            if right_result[1] == False:
                return (0, False)
            rt_ht += right_result[0]

        return (max(lt_ht, rt_ht), abs(lt_ht - rt_ht) <= 1)

