# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        q = collections.deque()

        q.append(root)
        q.append(None)

        res = []
        tmp = []
        i = 0

        while len(q) != 0:
            current = q.popleft()
            if current is None:
                i += 1
                if i % 2 == 0:
                    tmp.reverse()
                res.append(tmp)
                tmp = []
                if len(q) != 0:
                    q.append(None)
            else:
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)

                tmp.append(current.val)

        return res