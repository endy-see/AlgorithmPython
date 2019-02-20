"""
链表中倒数第k个节点
题目：输入一个链表，输出该链表中倒数第k个节点
思路：
方法1. 先数链表的个数n，然后从头走n-k即可，但是需要遍历链表2次
方法2. 双指针法，一个指针比另一个指针先走k-1步，只遍历链表1次
注意：代码的鲁棒性
"""


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 方法一：遍历链表2遍的方法
    def FindKthToTail(self, head, k):
        # write code here
        if not head or k < 1:
            return None

        link_len = 0
        cur = head
        while cur:
            link_len += 1
            cur = cur.next

        if k > link_len:
            return None

        cur = head
        cur_len = 1
        while cur_len != link_len-k+1:
            cur = cur.next
            cur_len += 1
        return cur

    # 方法二：双指针法，只需遍历一遍
    def FindKthToTail(self, head, k):
        if not head or k < 1:
            return None

        p_ahead = head
        p_behind = head
        cur_pos = 0
        while cur_pos < k:
            if not p_ahead:
                return None
            p_ahead = p_ahead.next
            cur_pos += 1
        # 两个指针同时走
        while p_ahead:
            p_ahead = p_ahead.next
            p_behind = p_behind.next
        return p_behind


obj = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4

# print(obj.FindKthToTail(node1, 1).val)
print(obj.FindKthToTail1(node1, 1).val)
