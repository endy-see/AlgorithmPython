"""
序列化二叉树
题目：请实现两个函数，分别用来序列化和反序列化二叉树
思路：
1. 怎么序列化就怎么反序列化（先or中or后）
2. 空节点不能漏掉，用特殊符号代替，如#替代None，另外为了便捷，序列化的时候每个节点后跟下划线_
"""

from collections import deque


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = ''

    def Serialize(self, root):
        # write code here
        if not root:
            return root
        self.serialize(root)
        return self.res

    # 先序的序列化
    def serialize(self, root):
        if not root:
            self.res += '#_'
            return
        else:
            self.res += str(root.val) + '_'
            self.serialize(root.left)
            self.serialize(root.right)

    def Deserialize(self, s):
        # write code here
        if not s or len(s) < 1:
            return None

        values = s.split('_')
        queue = deque()
        for i in range(0, len(values)):
            queue.append(values[i])
        return self.deserialize(queue)

    def deserialize(self, queue):
        value = queue.popleft()
        if value == '#':
            return None
        head = TreeNode(int(value))
        head.left = self.deserialize(queue)
        head.right = self.deserialize(queue)
        return head


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
# s = obj.Serialize(root)
# print(obj.Deserialize(s).val)

s = obj.Serialize(None)
print(s)
print(obj.Deserialize(s).val)
