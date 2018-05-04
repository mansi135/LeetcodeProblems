"""
103 - Zigzag level order

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

"""

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

#############################################################################################

"""
107 - Level Order from leef to root

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []

        q = collections.deque()

        res = []
        tmp = []

        q.append(root)
        q.append(None)

        while len(q) != 0:
            current = q.popleft()
            if current is None:
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

        res.reverse()

        return res

#############################################################################################

"""
102 -- Simple level order

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []

        q = collections.deque()

        res = []
        tmp = []

        q.append(root)
        q.append(None)

        while len(q) != 0:
            current = q.popleft()
            if current is None:
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
