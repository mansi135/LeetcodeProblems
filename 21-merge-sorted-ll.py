# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = new_list = ListNode(0)

        while l1 and l2:
            if l1.val <= l2.val:
                new_list.next = l1
                l1 = l1.next
            else:
                new_list.next = l2
                l2 = l2.next
            new_list = new_list.next

        # by end of this, only either l1 or l2 is left. If l1 or l2 are empty in the beginning, we reach here directly

        new_list.next = l1 or l2

        return dummy.next