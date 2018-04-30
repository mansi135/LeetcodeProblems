### If I Implement my own linkedList

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
       # self.prev = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self,value):
        n = Node(value)
        if self.tail == None:
            self.tail = n
            self.head = n
        else:
          #  self.head.prev = n
            n.next = self.head
            self.head = n

    def add_to_tail(self,value):
        n = Node(value)
        if self.head == None:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n

    def print(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

    # remove
    # size


dll = SinglyLinkedList()
# dll.add_to_head(3)
# dll.add_to_head(4)
dll.add_to_head(5)

dll1 = SinglyLinkedList()
# dll1.add_to_head(4)
# dll1.add_to_head(6)
dll1.add_to_head(5)


dll2 = SinglyLinkedList()

temp = dll.head
temp1 = dll1.head
carry = 0

while temp != None or temp1 != None:
    if temp1 == None:
        sum = temp.data + carry
    elif temp == None:
        sum = temp1.data + carry
    else:
        sum = temp.data + temp1.data + carry
    s = int(sum % 10)
    carry = int(sum / 10)
    dll2.add_to_tail(s)
    if(temp):
        temp = temp.next
    if(temp1):
        temp1 = temp1.next

if carry > 0:
    dll2.add_to_tail(carry)

dll2.print()



############################################# Alternate Solution for Leetcode######################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         # dll2 = SinglyLinkedList()
#
#         temp = l1
#         temp1 = l2
#         dummy = ListNode(0)
#         start = dummy
#         carry = 0
#
#         while temp != None or temp1 != None:
#             if temp1 == None:
#                 sum = temp.val + carry
#             elif temp == None:
#                 sum = temp1.val + carry
#             else:
#                 sum = temp.val + temp1.val + carry
#             s = int(sum % 10)
#             carry = int(sum / 10)
#             # dll2.add_to_tail(s)
#             new_node = ListNode(s)
#             dummy.next = new_node
#             dummy = new_node
#             if (temp):
#                 temp = temp.next
#             if (temp1):
#                 temp1 = temp1.next
#
#         if carry > 0:
#             dummy.next = ListNode(carry)
#         return start.next



