
import unittest
import collections


class BNode(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


    def zigzag_level_order(self):

        if not self:
            return []

        q = collections.deque()

        current = self
        q.append(None)

        tmp = []
        i = 0

        while len(q) != 0:
            if current is None:
                if i%2 == 0:
                    tmp.reverse()
                print(tmp)
                tmp = []
                q.append(None)
            else:
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
                # print(current.data, " ", end="")
                tmp.append(current.data)
            current = q.popleft()
            i += 1

        if i%2 != 0:
            tmp.reverse()

        print(tmp)

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
    tree.zigzag_level_order()


if __name__ == "__main__":
  unittest.main()