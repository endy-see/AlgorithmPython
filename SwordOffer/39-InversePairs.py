"""
数组中的逆序对
题目：在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对
输入一个数组，求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。
即输出P%1000000007

题目保证输入的数组中没有的相同的数字
数据范围：
对于%50的数据,size<=10^4
对于%75的数据,size<=10^5
对于%100的数据,size<=2*10^5
ex: [1, 2, 3, 4, 5, 6, 7, 0]，输出7

思想：归并排序 需要额外空间
注意：取模 否则无法通过oj
"""


# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.inverse_pair = 0

    def InversePairs(self, data):
        # write code here
        if not data or len(data) < 1:
            return 0

        self.merge_sort(data, 0, len(data) - 1)
        return self.inverse_pair

    def merge_sort(self, arr, left, right):
        if left == right:
            return
        mid = (left + right) // 2
        self.merge_sort(arr, left, mid)
        self.merge_sort(arr, mid + 1, right)
        self.merge(arr, left, mid, right)

    def merge(self, arr, left, mid, right):
        help = [0] * (right - left + 1)

        i = left
        j = mid + 1
        k = 0
        while i <= mid and j <= right:
            if arr[i] < arr[j]:
                help[k] = arr[i]
                self.inverse_pair += k-(i-left)
                if self.inverse_pair >= 1000000007:
                    self.inverse_pair %= 1000000007
                i += 1
            else:
                help[k] = arr[j]
                j += 1
            k += 1

        while i <= mid:
            help[k] = arr[i]
            self.inverse_pair += k - (i - left)
            k += 1
            i += 1

        while j <= right:
            help[k] = arr[j]
            k += 1
            j += 1

        for i in range(len(help)):
            arr[left+i] = help[i]


obj = Solution()
arr = [7, 6, 3, 5, 4, 8, 9]
print(obj.InversePairs(arr))