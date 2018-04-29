# Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth:

# all tests should start with test_

import unittest
import collections

class LinkedNode(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data) + ',' + str(self.next)



class BNode(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Like postorder traversal, append left, append right and then print self
# Called as Level-Order traversal

    def make_ll_of_all_depths(self):

        q = collections.deque()

        q.append(self)
        q.append(None)

        ll = ll_tail = LinkedNode(None)

        my_list = []



        while len(q) != 0:
            current = q.popleft()
            if current is None:
                print(ll)
                my_list.append(ll)
                if len(q) != 0:
                    ll = ll_tail = LinkedNode(None)
                    q.append(None)
            else:
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
                ll_tail.next = LinkedNode(current.data)
                ll_tail = ll_tail.next
                if ll.data is None:
                    ll = ll.next


        print(my_list)

        return my_list





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
    self.assertEqual(len(tree.make_ll_of_all_depths()), 4)


if __name__ == "__main__":
  unittest.main()