"""
删除链表中重复的节点
题目：在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
思路:
1. 删除链表中的节点：要么从头遍历，要么把下一个节点的内容复制到要删除的节点上覆盖原有的内容，再把下个节点删除
注：
 1)如果待删除的节点是链表的尾节点，那只能从头遍历着删除了；
 2)如果待删节点是链表的头节点，那删完后头节点应置None
 3)如果待删节点不在链表中
2. 删除链表中重复的节点
 1）头结点可能与后面的节点重复，即头结点可能被删
"""


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return pHead
        head1 = pHead.next
        if head1.val != pHead.val:
            pHead.next = self.deleteDuplication(pHead.next)
        else:
            while pHead.val == head1.val and head1.next is not None:
                head1 = head1.next
            if head1.val != pHead.val:
                pHead = self.deleteDuplication(head1)
            else:
                return None
        return pHead


obj = Solution()
head = ListNode(1)
ln1 = ListNode(1)
ln2 = ListNode(1)
ln3 = ListNode(2)
ln4 = ListNode(3)
ln5 = ListNode(4)
ln6 = ListNode(4)
ln7 = ListNode(5)
ln8 = ListNode(6)
ln9 = ListNode(6)
ln10 = ListNode(6)
head.next = ln1
ln1.next = ln2
ln2.next = ln3
ln3.next = ln4
ln4.next = ln5
ln5.next = ln6
ln6.next = ln7
ln7.next = ln8
ln8.next = ln9
ln9.next = ln10
res = obj.deleteDuplication(head)
while res:
    print(str(res.val)+' ')
    res = res.next