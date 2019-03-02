"""
数组中重复的数字
题目：在一个长度为n的数组里的所有数字都在0到n-1的范围内。数组中某些数字是重复的，
但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。
例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2
法1. 利用collection的Counter方法，对numbers中数（或字符串）做计数统计
法2. 利用题目信息，i位置上的数应该对应i，如果没对得上，就把i位置上的数调到其对应的位置上
"""


# -*- coding:utf-8 -*-
import collections


class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate1(self, numbers, duplication):
        # write code here
        flag = False
        c = collections.Counter(numbers)
        for k, v in c.items():
            if v > 1:
                duplication[0] = k
                flag = True
                break
        return flag

    # 试图把numbers调整顺序 把不是i位置上的数调走，把是i位置上的数调过来
    def duplicate(self, numbers, duplication):
        # write code here
        for i in range(len(numbers)):
            if numbers[i] != i:
                temp = numbers[numbers[i]]
                if temp == numbers[i]:
                    duplication[0] = numbers[i]
                    return True
                else:
                    numbers[numbers[i]] = numbers[i]
                    numbers[i] = temp
                    i -= 1
        return False


obj = Solution()
arr = [2, 3, 1, 0, 2, 5, 3]
print(obj.duplicate(arr, [0]*len(arr)))
