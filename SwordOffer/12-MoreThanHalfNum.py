"""
题目：
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
方法一：快排partition思想，时间复杂度O(n)
方法二：根据数组特点找出时间复杂度O(n)的算法
数组中有一个数字出现的次数超过数组长度的一般，也就是说它出现的次数比其他所有数字出现次数的和还要多
因此可以考虑在遍历数组的时候保存两个值：一个是数组中的一个数字；另一个是次数。当遍历到下一个数字的
时候，如果下一个数字和我们之前保存的数字相同，则次数加1；如果下一个数字和我们之前保存的数字不同，
则次数减1.如果次数为0，那么我们需要保存下一个数字，并把次数设为1.由于我们要找的数字出现的次数
比其他所有数字出现的次数之和还要多，那么要找的数字肯定是最后一次把次数设为1时的对应数字
"""
import random


# -*- coding:utf-8 -*-
class Solution:
    # 方法二：根据数组特点找出时间复杂度O(n)的算法
    def MoreThanHalfNum_Solution1(self, numbers):
        if not numbers or len(numbers) < 1:
            return 0
        val = numbers[0]
        count = 1
        for i in range(1, len(numbers)):
            if numbers[i] == val:
                count += 1
            else:
                count -= 1
                if count == 0:
                    val = numbers[i]
                    count = 1
            # i += 1
        if count >= 1 and self.check_more_than_half(numbers, val):
            return val
        return 0

    def check_more_than_half(self, arr, val):
        count = 0
        for i in range(0, len(arr)):
            if arr[i] == val:
                count += 1
        if count*2 > len(arr):
            return True
        else:
            return False

    # 方法一：快排的partition思想
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers or len(numbers) < 1:
            return 0
        return self.find_more_than_half_num(numbers, 0, len(numbers) - 1)

    def find_more_than_half_num(self, arr, left, right):
        if left > right:
            return 0

        index = int(left + random.random() * (right - left + 1))
        self.swap(arr, right, index)
        small_big = self.partition(arr, left, right - 1, arr[right])
        self.swap(arr, right, small_big[1])
        # small_big[1]目前是等于anchor的，大于anchor的位置应该是small_big[1]+1位置
        if (small_big[1] + 1) - small_big[0] - 1 > len(arr) / 2:
            return arr[small_big[1]]

        # 接着对大于一半的一边继续找
        if small_big[0] > len(arr) / 2:
            return self.find_more_than_half_num(arr, left, small_big[0])
        else:
            return self.find_more_than_half_num(arr, small_big[1] + 1, right)

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
# arr = [1, 2, 3, 2, 2, 2, 5, 4, 2]
# arr = [1, 2, 3, 2, 4, 2, 5, 2, 3]
arr = [2, 2, 2, 2, 2, 1, 3, 4, 5]
# arr = [1]
print(obj.MoreThanHalfNum_Solution1(arr))
