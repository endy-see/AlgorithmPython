"""
包含min函数的栈
题目：定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数
时间复杂度O(1)
"""


# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack_data = []
        self.stack_min = []

    def push(self, node):
        # write code here
        # 插入一个数，要同步插入一个最小值
        self.stack_data.append(node)
        if not self.stack_min or node <= self.min():
            self.stack_min.append(node)

    def pop(self):
        # write code here
        # 弹出数
        if not self.stack_data:
            return None
        res = self.stack_data.pop()
        if res == self.min():
            self.stack_min.pop()
        return res

    def top(self):
        # write code here
        if not self.stack_data:
            return None
        return self.stack_min[-1]

    def min(self):
        # write code here
        if not self.stack_min:
            return None
        return self.stack_min[-1]


obj = Solution()
obj.push(3)
print(obj.min())
obj.push(4)
print(obj.min())
obj.push(2)
print(obj.min())
obj.push(3)
print(obj.min())
