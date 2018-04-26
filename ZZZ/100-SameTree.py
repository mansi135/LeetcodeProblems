# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def isSameTree(self, p, q):

        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


    #2* O(n) space using BFS
    def isSameTree1(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        p_queue = self.bfs(p)
        q_queue = self.bfs(q)

        print(p_queue)
        print(q_queue)

        return p_queue == q_queue

    def bfs(self, root):

        root_q = [root]

        if not root:
            return [None]
        else:
            values_q = [root.val]

        i = 0

        while i < len(root_q):
            if root_q[i].left:
                root_q.append(root_q[i].left)
                values_q.append(root_q[i].left.val)
            elif not root_q[i].left:
                values_q.append(None)
            if root_q[i].right:
                root_q.append(root_q[i].right)
                values_q.append(root_q[i].right.val)
            elif not root_q[i].right:
                values_q.append(None)

            i += 1

        return values_q


