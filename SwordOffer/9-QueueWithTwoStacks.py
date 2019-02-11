"""
题目描述：
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型
"""


# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        # write code here
        self.stack1.append(node)

    def pop(self):
        if not self.stack1 and not self.stack2:
            return None

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def peek(self):
        if not self.stack1 and not self.stack2:
            return None

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[len(self.stack2)-1]


obj = Solution()
print(obj.pop())
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.pop())
obj.push(4)
obj.push(5)
print(obj.peek())
print(obj.pop())




