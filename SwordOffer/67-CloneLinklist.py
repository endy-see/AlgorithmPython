"""
复杂链表的复制
题目：输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
思路1.复制原始链表上的每个节点，并用next链接起来；然后设置每个节点的sibling指针，
由于每次找sibling都要从头开始找，所以时间复杂度O(n)
思路2.空间换时间。还是先复制链表，然后用O(n)的哈希表保存复制的元素链表上的每个节点N'，即<N，N'>；设置链表上每个节点的sibling O(n)
思路3. O(n)的解法
    1)先沿着链表复制每个节点（复制节点在原节点的后面）
    2）给slibling赋值
    3）把复制节点拆出来
"""


# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return pHead

        # 复制原链表中的每个节点 并接到该节点的后面
        cur_node = pHead
        next_node = pHead.next
        while next_node:
            new_node = RandomListNode(cur_node.label)
            new_node.next = next_node
            cur_node.next = new_node
            cur_node = next_node
            next_node = cur_node.next
        cur_node.next = RandomListNode(cur_node.label)

        # 给clone的各个节点赋值random节点
        cur_node = pHead
        new_cur_node = pHead.next
        while cur_node:
            if cur_node.random:
                new_cur_node.random = cur_node.random.next
            cur_node = new_cur_node.next
            if cur_node:
                new_cur_node = cur_node.next

        # 将链表分开成两个链表
        cur_node = pHead
        pNewHead = pHead.next
        new_cur_node = pNewHead
        while cur_node:
            cur_node.next = new_cur_node.next
            cur_node = cur_node.next
            if cur_node:
                new_cur_node.next = cur_node.next
                new_cur_node = new_cur_node.next
        return pNewHead


head = RandomListNode(1)
n1 = RandomListNode(2)
n2 = RandomListNode(3)
n3 = RandomListNode(4)
n4 = RandomListNode(5)
head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n2.random = n1
n3.random = head
head.random = n4
obj = Solution()
print(obj.Clone(head).label)


