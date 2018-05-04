import collections

# Definition for a binary tree node.
class BNode(object):

    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def get_level(node, root):

    if not root:
        return 0

    q = collections.deque()

    q.append((root, 1))

    while len(q) != 0:
        current = q.popleft()
        if current[0].val == node:
            return current[1]
        else:
            if current[0].left:
                q.append((current[0].left, current[1]+1))
            if current[0].right:
                q.append((current[0].right, current[1]+1))

    return -1


tree = BNode(3,
                 BNode(2,
                       BNode(1),
                       BNode(4)
                       ),
                 BNode(5)

                 )

print(get_level(5, tree))