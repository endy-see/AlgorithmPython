"""
从上往下打印二叉树
题目：从上往下打印出二叉树的每个节点，同层节点从左至右打印
思路：二叉树的层序遍历 借助队列
"""

from collections import deque


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        res = []
        if not root:
            return res

        queue = deque()
        # 右进左出
        queue.append(root)
        while queue:
            cur_node = queue.popleft()
            res.append(cur_node.val)
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        return res
