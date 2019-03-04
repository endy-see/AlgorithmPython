"""
队列的最大值
题目：请定义一个队列并实现函数max得到队列里的最大值，要求函数max、push、pop的时间复杂度都是O(1)
思路：双端队列
1）要寻找队列的最大值，相当于将滑动窗口设置为整个队列
2）这里需要使用两个队列，一个队列用来保存入队的数据，一个队列用来保存队列的当前最大值
3）注意出队操作，数据队列出队的同时需要判断其索引是否和当前最大值队列首部索引相同，
   如果相同则同时也将最大值队列头部出队
"""

from collections import deque


class InternalData:
    def __init__(self, x, i):
        self.val = x
        self.index = i


class Solution:
    def __init__(self):
        self.data_queue = deque()
        self.max_index_queue = deque()
        self.cur_index = 0

    # 左边入队
    def push(self, num):
        # 当前入队的数大于最大索引队列中左侧最小索引所对应的值，则循环删除索引队列中的索引
        # 直到遇到一个比当前数大的索引 停止
        while self.max_index_queue and num >= self.max_index_queue[0].val:
            self.max_index_queue.popleft()

        # 构建数据节点 分别插入到数据队列和索引队列中
        internal_data = InternalData(num, self.cur_index)
        self.data_queue.appendleft(internal_data)
        self.max_index_queue.appendleft(internal_data)

        self.cur_index += 1

    # 右边出队
    def pop(self):
        if not self.max_index_queue:
            return None
        if self.max_index_queue[-1].index == self.data_queue[-1].index:
            self.max_index_queue.pop()
        return self.data_queue.pop()

    # 获取当前队列最大值
    def max(self):
        if not self.max_index_queue:
            return None
        return self.max_index_queue[-1].val


obj = Solution()
obj.push(3)
obj.push(8)
obj.push(4)
print(obj.max())
print(obj.pop())
print(obj.max())
print(obj.pop())
print(obj.max())
print(obj.pop())
print(obj.max())
obj.push(5)
obj.push(2)
obj.push(6)
obj.push(1)
obj.push(9)
print('a')
