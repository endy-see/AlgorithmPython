"""
合并两个排序的链表
题目：
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
"""


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1 and not pHead2:
            return pHead1
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1

        if pHead1.val < pHead2.val:
            p_new_head = pHead1
            pHead1 = pHead1.next
        else:
            p_new_head = pHead2
            pHead2 = pHead2.next

        p_new_head_cur_node = p_new_head
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                cur_node = pHead1
                pHead1 = pHead1.next
            else:
                cur_node = pHead2
                pHead2 = pHead2.next
            p_new_head_cur_node.next = cur_node
            p_new_head_cur_node = cur_node

        if pHead1:
            p_new_head_cur_node.next = pHead1
        if pHead2:
            p_new_head_cur_node.next = pHead2
        return p_new_head