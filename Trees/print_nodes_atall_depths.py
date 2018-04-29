# Given a binary tree, print nodes at each depth:

# all tests should start with test_

import unittest
import collections


class BNode(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Like postorder traversal, append left, append right and then print self
# Called as Level-Order traversal

    def make_ll_of_all_depths(self):

        q = collections.deque()

        current = self
        q.append(None)

        while len(q) != 0:
            if current == None:
                print()
                q.append(None)
            else:
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
                print(current.data, " ", end="")
            current = q.popleft()


class MyTreeTestCases(unittest.TestCase):

  def test_list_of_depths(self):

    tree = BNode(1,
                 BNode(2,
                       BNode(4),
                       BNode(5,
                             BNode(8)
                             )
                        ),
                 BNode(3,
                       BNode(6,
                             None,
                             BNode(9)
                             ),
                       BNode(7,
                             BNode(10))
                       )
                 )
    tree.make_ll_of_all_depths()


if __name__ == "__main__":
  unittest.main()