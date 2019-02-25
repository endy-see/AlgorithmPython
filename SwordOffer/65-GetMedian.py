"""
数据流中的中位数
题目：如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值
排序之后位于中间的数值。如果从数据流中读取偶数个数值，那么中位数就是所有数值排序之后中间
两个数的平均值。我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数
思路：用两个堆，一个大根堆和一个小根堆
大根堆：负责记录中位数左侧的值，其堆顶表示中位数（即左侧最大数）
小根堆：负责记录中位数右侧的值，如果流中元素个数为偶数时，其堆顶也是中位数（表示右侧最小数）
"""

import heapq


# -*- coding:utf-8 -*-
class BigHeap:
    def __init__(self):
        self.arr = list()

    def heap_insert(self, val):
        heapq.heappush(self.arr, -val)

    def heapify(self):
        heapq.heapify(self.arr)

    def heap_pop(self):
        return -heapq.heappop(self.arr)

    def get_top(self):
        if not self.arr:
            return None
        return -self.arr[0]

    def get_len(self):
        return len(self.arr)


class Solution:
    def __init__(self):
        self.count = 0
        self.max_heap = BigHeap()
        self.min_heap = []

    def modify_two_heap_size(self):
        if self.max_heap.get_len() == len(self.min_heap) + 2:
            self.min_heap.append(self.max_heap.heap_pop())
        if len(self.min_heap) == self.max_heap.get_len() + 2:
            heapq.heapify(self.min_heap)
            self.max_heap.heap_insert(self.min_heap.pop())

    def Insert(self, num):
        # write code here
        # 先向大根堆中插入当前数 如果左侧堆中元素的数量-右侧堆中元素数量大于1 则把左侧堆顶放到右侧堆中
        max_heap_size = self.max_heap.get_len()
        min_heap_size = len(self.min_heap)

        max_heap_head = self.max_heap.get_top()

        if max_heap_size == 0:
            self.max_heap.heap_insert(num)
            return
        if max_heap_head >= num:
            self.max_heap.heap_insert(num)
        else:
            if min_heap_size == 0:
                self.min_heap.append(num)
                return
            heapq.heapify(self.min_heap)
            if self.min_heap[0] > num:
                self.max_heap.heap_insert(num)
            else:
                self.min_heap.append(num)
        self.modify_two_heap_size()

    def GetMedian(self, n=None):
        # write code here
        max_heap_size = self.max_heap.get_len()
        min_heap_size = len(self.min_heap)
        if max_heap_size == 0:
            return None

        if (max_heap_size + min_heap_size) & 1 == 0:
            heapq.heapify(self.min_heap)
            return (self.max_heap.get_top() + self.min_heap[0])*0.5

        if max_heap_size > min_heap_size:
            return self.max_heap.get_top()
        else:
            heapq.heapify(self.min_heap)
            return self.min_heap[0]


obj = Solution()
obj.Insert(5)
print(obj.GetMedian())
obj.Insert(2)
print(obj.GetMedian())
obj.Insert(3)
print(obj.GetMedian())
obj.Insert(4)
print(obj.GetMedian())
obj.Insert(1)
print(obj.GetMedian())
obj.Insert(6)
print(obj.GetMedian())
obj.Insert(7)
print(obj.GetMedian())
obj.Insert(0)
print(obj.GetMedian())
obj.Insert(8)
print(obj.GetMedian())