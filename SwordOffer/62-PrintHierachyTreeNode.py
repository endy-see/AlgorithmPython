"""
把二叉树打印成多行
思路：从上到下按层打印二叉树，同一层节点从左至右输出。每一层输出一行
"""

from collections import deque


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []

        result = []
        queue = deque()
        # 默认定义：右侧入队、左侧出队
        queue.append(pRoot)
        last_count = 1
        cur_count = 0
        while len(queue) > 0:
            res = []
            while last_count != 0:
                cur_node = queue.popleft()
                res.append(cur_node.val)
                if cur_node.left:
                    queue.append(cur_node.left)
                    cur_count += 1
                if cur_node.right:
                    queue.append(cur_node.right)
                    cur_count += 1
                last_count -= 1
            result.append(res)
            last_count = cur_count
            cur_count = 0
        return result


