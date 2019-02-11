"""
题目描述：
用两个队列来实现一个栈，完成栈的Push和Pop操作。
栈中的元素为int类型

思路：
push操作：只往queue队中添加元素
pop操作：每次会把queue中的N-1个元素依次加入到help，
然后从queue中弹出最后一个元素，再交换queue和help
peek操作：基本和pop操作类似，但是queue的最后一个元素
看完后还要再加到help中
"""


# -*- coding:utf-8 -*-
class StackWithTwoQueue:
    def __init__(self):
        self.queue = []
        self.help = []

    def push(self, node):
        # write code here
        # 队列：先进先出
        self.queue.insert(0, node)

    def pop(self):
        # 现出现整
        if self.queue:
            while len(self.queue) != 1:
                self.help.insert(0, self.queue.pop())

            res = self.queue.pop()
            self.swap()
            return res
        return None

    def peek(self):
        # 看完后还是要再加入到队列中的
        if self.queue:
            while len(self.queue) != 1:
                self.help.insert(0, self.queue.pop())
            res = self.queue.pop()
            self.help.insert(0, res)
            self.swap()
            return res
        return None

    def swap(self):
        tmp = self.queue
        self.queue = self.help
        self.help = tmp


obj = StackWithTwoQueue()
# print(obj.pop())
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.peek())
obj.push(4)
obj.push(5)
print(obj.pop())
print(obj.peek())
print(obj.pop())
print(obj.pop())
