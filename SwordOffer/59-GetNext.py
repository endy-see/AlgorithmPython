"""
二叉树的下一个节点
题目：
给定一个二叉树和其中的一个节点，请找出中序遍历顺序的下一个节点并返回。
注意，树中的节点不仅包含左右子节点，同时包含指向父节点的指针
思路：
1. 如果当前节点有右子树，那么当前节点的下一个节点就是其右子树最左的节点
2. 如果当前节点没有右子树，看当前节点是否是其父的左孩子
 1）如果是其父的左孩子，则下一个节点就是其父节点
 2）如果不是其父的左孩子，则循环向上，直到找到一个节点是其父左孩子的节点，
    其父就是当前节点的下一个节点（如果当找到最后一个节点，直接返回None即可）
"""


# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return pNode

        if pNode.right:
            cur_node = pNode.right
            while cur_node.left:
                cur_node = cur_node.left
            return cur_node
        else:
            cur_node = pNode
            parent = pNode.next
            if not parent or parent.left == pNode:
                return parent
            else:
                while parent and parent.left != cur_node:
                    cur_node = parent
                    parent = parent.next
                return parent
