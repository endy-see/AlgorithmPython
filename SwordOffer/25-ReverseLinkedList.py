"""
反转链表
题目：输入一个链表，反转链表后，输出新链表的表头。
思想：扭转链表中指针指向即可
"""


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def ReverseList(self, pHead):
        if not pHead or not pHead.next:
            return pHead

        p_new_head = None           # 反转后链表的头结点
        cur_node = pHead            # 当前节点
        while cur_node:
            next_node = cur_node.next  # 保存当前节点的下一个节点 放在链表丢失
            cur_node.next = p_new_head
            p_new_head = cur_node
            cur_node = next_node
        return p_new_head
