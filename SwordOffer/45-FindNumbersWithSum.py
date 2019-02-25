"""
和为s的两个数字
题目：输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。
如果有多对数字的和等于s，输出两个数的乘积最小的
思路：双指针问题 一个small，一个big
"""

# -*- coding:utf-8 -*-
import sys


class Solution:
    def __init__(self):
        self.max_multi = sys.maxsize
        self.res = []

    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array or len(array) < 1:
            return []
        small = 0
        big = len(array) - 1
        while small < big:
            if array[small] + array[big] < tsum:
                small += 1
            elif array[small] + array[big] > tsum:
                big -= 1
            else:
                if array[small] * array[big] < self.max_multi:
                    self.max_multi = array[small] * array[big]
                    self.res = [array[small], array[big]]
                small += 1
                big -= 1
        return self.res


obj = Solution()
# arr = [1, 2, 4, 7, 11, 15]
arr = [1, 2, 4, 7, 11, 16]
print(obj.FindNumbersWithSum(arr, 10))
