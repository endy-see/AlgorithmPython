# 输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 方法二：基于递归的方法(递归本质上就是一个栈结构)
    # 要实现反过来输出链表，每访问一个节点的时候，先递归输出它后面的节点，
    # 再输出该节点自身，这样链表的输出结果就反过来了
    def printList(self, listNode, res):
        if listNode:
            self.printList(listNode.next, res)
            res.append(listNode.val)
        return res

    def printListFromTailToHead(self, listNode):
        return self.printList(listNode, [])

    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead1(self, listNode):
        # write code here
        stack = []
        while listNode:
            stack.append(listNode)
            listNode = listNode.next
        res = []
        while stack:
            res.append(stack.pop().val)
        return res


obj = Solution()
node1 = ListNode(58)
node2 = ListNode(24)
node3 = ListNode(0)
node4 = ListNode(67)

node1.next = node2
node2.next = node3
node3.next = node4

print(obj.printListFromTailToHead(node1))
