"""
链表中环的入口节点：
题目：给一个链表，若其中包含环，请找出该链表的环的入口节点，否则，输出null
"""


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        # 先判断是否有环 然后再判断入环节点
        if not pHead or not pHead.next or not pHead.next.next:
            return None
        p_slow = pHead.next
        p_fast = pHead.next.next

        is_loop = False
        while p_fast.next and p_fast.next.next:
            if p_slow == p_fast:
                is_loop = True
                break
            p_slow = p_slow.next
            p_fast = p_fast.next.next

        if is_loop:
            p_fast = pHead
            while p_fast != p_slow:
                p_slow = p_slow.next
                p_fast = p_fast.next
            return p_slow
        else:
            return None
