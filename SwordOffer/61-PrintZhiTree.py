"""
按之字形顺序打印二叉树
题目：请实现一个函数按照之字形打印二叉树，即第一层按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，第三层按照从左到右的顺序打印，其他层以此类推
思路：
1. 两个栈实现 -> 逻辑清晰 快 容易写
2. 用双端队列 用flag控制打印方向（好是好，但是不知道什么时候该遍历下一层，这种方法先放着吧）
flag=True  从左往右打印 从左边弹出节点 从右边加入其孩子节点 先入左孩子再入右孩子
flag=False 从右往左打印 从右边弹出节点 从左边加入其孩子节点 先入右孩子再入左孩子
count 记录每次打印的节点个数
"""

from collections import deque


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []

        result = []
        res = []
        left_to_right_list = []
        right_to_left_list = []
        left_to_right_list.append(pRoot)
        while len(left_to_right_list) != 0 or len(right_to_left_list) != 0:
            while left_to_right_list:
                cur_node = left_to_right_list.pop()
                res.append(cur_node.val)
                if cur_node.left:
                    right_to_left_list.append(cur_node.left)
                if cur_node.right:
                    right_to_left_list.append(cur_node.right)
            if len(res) != 0:
                result.append(res)
                res = []
            while right_to_left_list:
                cur_node = right_to_left_list.pop()
                res.append(cur_node.val)
                if cur_node.right:
                    left_to_right_list.append(cur_node.right)
                if cur_node.left:
                    left_to_right_list.append(cur_node.left)
            if len(res) != 0:
                result.append(res)
                res = []
        return result

    def Print1(self, pRoot):
        # write code here
        if not pRoot:
            print('None')

        queue = deque()
        queue.append(pRoot)
        is_end = False
        flag = True
        while len(queue) != 0:
            # 从左往右打印 从队列左边出节点
            if flag:
                node = queue.popleft()
                is_end = True
                queue.append(node.left)
                queue.append(node.right)
                flag = False
            else:
                print('not finished!')


obj = Solution()
obj = Solution()
root = TreeNode(8)
tn1 = TreeNode(6)
tn2 = TreeNode(9)
root.left = tn1
root.right = tn2
tn3 = TreeNode(5)
tn4 = TreeNode(7)
tn1.left = tn3
tn1.right = tn4
tn5 = TreeNode(7)
tn6 = TreeNode(5)
tn2.left = tn5
tn2.right = tn6
print(obj.Print(root))
