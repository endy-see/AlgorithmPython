"""
两个链表的第一个公共节点
题目：输入两个链表，找出它们的第一个公共节点。
思路：
1. 两条链表都是单向无环链表
2. 一条有环， 一条无环
3. 两个链表都有环时：
    1）入环节点相同时，需要从头找到两条链表相交的第一个节点
    2）两个链表的入环节点不同时（各自为环），可能根本不相交，也可能角点出现在环上
"""


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def GetIntersectNode(self, head1, head2):
        # write code here
        if not head1 or not head2:
            return None
        loop1 = self.get_loop_node(head1)
        loop2 = self.get_loop_node(head2)
        # 两条链表都无环
        if not loop1 and loop2:
            # return self.FindFirstCommonNodeWithNoHoop(head1, head2)
            return self.no_loop(head1, head2)
        # 一条有环一条无环时，不可能有交点
        # 两条都有环时
        if loop1 and loop2:
            return self.both_loop(head1, loop1, head2, loop2)
        return None

    # 获取第一个入环节点
    def get_loop_node(self, head):
        # 只有一个节点或只有两个节点，都无法形成环（环至少得3个节点）
        if not head.next or not head.next.next:
            return None
        # 慢指针
        n1 = head.next
        # 快指针
        n2 = head.next.next
        while n1 != n2:
            if not n2.next or not n2.next.next:
                return None
            n2 = n2.next.next
            n1 = n1.next
        # 如果能走到这一步，说明一定有环
        # 快指针重回头结点，然后与慢指针同步走
        n2 = head
        while n1 != n2:
            n1 = n1.next
            n2 = n2.next
        return n1

    # 在非常确定两条链表是单向无环链表时，有两种方法：一种用栈，另一种是统计长度、先走几步的问题（
    # 这里推荐第二种，可以省空间
    def FindFirstCommonNodeWithNoHoop(self, pHead1, pHead2):
        len1 = 0
        len2 = 0
        p1 = pHead1
        p2 = pHead2
        while p1:
            len1 += 1
            p1 = p1.next
        while p2:
            len2 += 1
            p2 = p2.next

        if len1 > len2:
            long = pHead1
            short = pHead2
        else:
            long = pHead2
            short = pHead1

        pre_step = 0
        while pre_step < abs(len1-len2):
            long = long.next
            pre_step += 1

        while long and short:
            if long.val == short.val:
                return long
            long = long.next
            short = short.next
        return None

    def no_loop(self, head1, head2):
        if not head1 or not head2:
            return None
        cur1 = head1
        cur2 = head2
        n = 0
        while cur1.next:
            n += 1
            cur1 = cur1.next
        while cur2.next:
            n -= 1
            cur2 = cur2.next
        # 如果两条链表最后一个元素都不相等，说明两条链表根本就不想交
        if cur1 != cur2:
            return None
        if n > 0:
            cur1 = head1
            cur2 = head2
        else:
            cur1 = head2
            cur2 = head1
        n = abs(n)
        while n != 0:
            n -= 1
            cur1 = cur1.next
        while cur1 != cur2:
            cur1 = cur1.next
            cur2 = cur2.next
        return cur1

    def both_loop(self, head1, loop1, head2, loop2):
        if loop1 == loop2:
            # 入环节点相同（环外相交）但是两条链表不一样长度时 还是需要从头找第一个相交节点的
            cur1 = head1
            cur2 = head2
            n = 0
            while cur1 != loop1:
                n += 1
                cur1 = cur1.next
            while cur2 != loop2:
                n -= 1
                cur2 = cur2.next
            # cur1、cur2再分别重新指向较长、较短的链表
            if n > 0:
                cur1 = head1
                cur2 = head2
            else:
                cur1 = head2
                cur2 = head1
            n = abs(n)
            # cur1在长链表中先走n步
            while n != 0:
                n -= 1
                cur1 = cur1.next
            while cur1 != cur2:
                cur1 = cur1.next
                cur2 = cur2.next
            return cur1
        else:
            # 入环节点不同（可能各自为环，也可能共用一个环）
            cur1 = loop1.next
            while cur1 != loop1:
                if cur1 == loop2:
                    return loop1
            return None




