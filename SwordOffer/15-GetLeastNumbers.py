"""
最小的K个数
题目：输入n个整数，找出其中最小的K个数。
例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4
方法一：快排
方法二：堆
"""
import random
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

    def heap_replace(self, val):
        if self.get_top() > val:
            # heapq.heappop(self.arr)
            # heapq.heappush(self.arr, -val)
            heapq.heapreplace(self.arr, -val)

    def get_heap(self):
        res = []
        for i in range(0, len(self.arr)):
            res.append(self.get_top())
            self.heap_pop()
        res.reverse()
        return res

    def get_top(self):
        if not self.arr:
            return
        return -self.arr[0]


class Solution:
    # 方法一：快排的partition思想
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput or len(tinput) < k:
            return []
        # 此题的诡异之处在于，返回的前k个数必须有序 时间复杂度O(n)
        # 正常来说，如果不要求有序，那直接返回res即可
        res = self.get_least_numbers(tinput, 0, len(tinput) - 1, k)
        self.quick_sort(res, 0, len(res) - 1)
        return res

    # 方法二：堆排的思想nlog(n)（但是不写具体的堆排序，而是直接采用heap数据结构）
    def GetLeastNumbers_Solution1(self, tinput, k):
        if not tinput or len(tinput) < k:
            return []
        return heapq.nsmallest(k, tinput)

    # 方法三：堆排nlog(k) 需要用到大根堆
    def GetLeastNumbers_Solution2(self, tinput, k):
        if not tinput or len(tinput) < k:
            return []
        big_heap = BigHeap()
        for i in range(0, k):
            big_heap.heap_insert(tinput[i])

        for i in range(k, len(tinput)):
            big_heap.heap_replace(tinput[i])
        return big_heap.get_heap()

    def quick_sort(self, arr, left, right):
        if left > right:
            return
        index = int(left + random.random() * (right - left + 1))
        self.swap(arr, index, right)
        small_big = self.partition(arr, left, right - 1, arr[right])
        self.swap(arr, small_big[1], right)
        self.quick_sort(arr, left, small_big[0])
        self.quick_sort(arr, small_big[1] + 1, right)

    def get_least_numbers(self, arr, left, right, k):
        if left > right:
            return None
        index = k - 1
        # index = int(left + random.random() * (right - left + 1))
        self.swap(arr, index, right)
        small_big = self.partition(arr, left, right - 1, arr[right])
        self.swap(arr, small_big[1], right)
        if small_big[0] > k - 1:
            # 前k小的数在small_big[0]的左边
            return self.get_least_numbers(arr, left, small_big[0], k)
        elif small_big[0] == k - 1:
            return arr[:small_big[0] + 1]
        elif small_big[1] > k - 1:
            # 说明中间相等部分可以补充前k个数中不足k个的部分
            return arr[:k]
        elif small_big[1] == k - 1:
            return arr[:small_big[1] + 1]
        else:
            return self.get_least_numbers(arr, small_big[1] + 1, right, k)

    def swap(self, arr, i, j):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp

    def partition(self, arr, left, right, anchor):
        small = left - 1
        big = right + 1
        cur = left
        while cur != big:
            if arr[cur] < anchor:
                self.swap(arr, small + 1, cur)
                small += 1
                cur += 1
            elif arr[cur] > anchor:
                self.swap(arr, big - 1, cur)
                big -= 1
            else:
                cur += 1
        return [small, big]


obj = Solution()
arr1 = [1, 2, 3, 2, 2, 2, 5, 4, 2]
# print(obj.GetLeastNumbers_Solution(arr, 4))
arr = [4, 5, 1, 6, 2, 7, 3, 8]
print(obj.GetLeastNumbers_Solution2(arr, 4))
