"""
python中堆的使用　使用heapq构建小根堆和大根堆
python默认的heapq模块只支持最小堆的构建
"""

import heapq

"""
heapq中的pop和push等操作会自动调用heapify方法调整堆．除了下面方法，还有一些常用的方法：
heappushpop: 相当于先执行了heappush(heap, data),再执行了heappop(heap)
heapreplace: 相当于先执行了heappop(heap),再执行了heappush(heap, data)
nlargest/nsmallest:　求堆中最大/最小的k个元素
merge: 输入是两个有序的数组　输出是数组合并后的有序的数组（注：如果输入无序，那么输出也不会保证有序）

大根堆：python的heapq是不支持大根堆的，但是有一个巧妙的实现：
我们还是用小根堆来进行逻辑操作，在做push的时候，把当前数的相反数存进去
例如，如果存进去的数是最大值，那么取它的相反数时就是最小值，仍然是堆顶元素）
在访问堆顶的时候，再对它取反，就获取到了最大数
"""


class SmallHeap:
    def __init__(self):
        self.arr = list()

    def heap_insert(self, data):
        heapq.heappush(self.arr, data)

    def heapify(self):
        heapq.heapify(self.arr)

    def heap_pop(self):
        return heapq.heappop(self.arr)

    def heap_top(self):
        if not self.arr:
            return
        return self.arr[0]

    def get_heap_nlargest(self, n):
        if not self.arr:
            return
        return heapq.nlargest(n, self.arr)

    def get_heap_nsmallest(self, n):
        if not self.arr:
            return
        return heapq.nsmallest(n, self.arr)


class BigHeap:
    def __init__(self):
        self.arr = list()

    def heap_insert(self, data):
        heapq.heappush(self.arr, -data)

    def heapify(self):
        heapq.heapify(self.arr)

    def heap_pop(self):
        return -heapq.heappop(self.arr)

    def heap_top(self):
        if not self.arr:
            return
        return -heapq[0]


if __name__ == '__main__':
    small_heap = SmallHeap()
    small_heap.heap_insert(5)
    small_heap.heap_insert(3)
    small_heap.heap_insert(8)
    small_heap.heap_insert(6)
    small_heap.heap_insert(2)
    small_heap.heap_insert(4)
    small_heap.heap_insert(9)
    small_heap.heap_insert(1)
    print(small_heap.get_heap_nlargest(3))
    print(small_heap.get_heap_nsmallest(3))