class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


def swapPairs(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """

    node = head
    prev = head

    if head and head.next:
        head = head.next

    while node and node.next:
        tmp = node.next.next
        prev.next = node.next

        node.next.next = node

        node.next = tmp
        prev = node
        node = tmp

    return head


def printme(h):

    tmp = h
    while tmp:
        print(tmp.val, end="")
        tmp = tmp.next

#h = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
#h = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
h = ListNode(1, ListNode(2, ListNode(3,ListNode(4, ListNode(5)))))

printme(h)

print()
printme(swapPairs(h))