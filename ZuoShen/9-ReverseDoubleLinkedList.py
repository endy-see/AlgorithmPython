"""
反转双向链表
要求：如果链表长度为N，时间复杂度要求为O(N)，额外空间复杂度为O(1)
"""


class DoubleNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.last = None


def reverse_double_linkedlist(head):
    if not head or not head.next:
        return head

    new_head = None
    cur = head
    while cur:
        next = cur.next
        cur.next = new_head
        cur.last = next
        new_head = cur
        cur = next
    return new_head



