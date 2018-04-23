# given n is always valid

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



def remove_nth(head, n):

    if n == 0:
        return None

    diff = 0

    tmp = head
    tmp_nth = head

    while tmp.next is not None:
        if diff == n:
            break
        else:
            diff += 1
            tmp = tmp.next

    while tmp.next is not None:
        tmp = tmp.next
        tmp_nth = tmp_nth.next

    # removing
    # there is possiblity that diff is still less and we are the first node to be removed,
    # in that case just move the head
    if diff == n:
        tmp_nth.next = tmp_nth.next.next
    else:
        head = head.next

    return head



ll = ListNode(1)
ll.next = ListNode(2)
ll.next.next = ListNode(3)

r = remove_nth(ll, 1)



print(r)