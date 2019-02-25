"""
连续子数组的最大和
题目：输入一个整型数组，数组里面有正数也有负数。数组中的一个或连续多个
整数组成一个子数组。返回它的最大连续子数组的和。要求时间复杂度为O(n)
ex: [6,-3,-2,7,-15,1,2,2] 连续子数组的最大和为8（index从0到3）
思路：如果当前数组和小于等于0，则连续子数组的重新从当前位置i开始计数
如果当前数组和大于0，就加上当前值（当然，加上当前值后cur_sum可能变大，
也可能变小，但是都留到下次去更新吧）；更新最大和
"""

import sys


# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return []
        max_sum = -sys.maxsize
        cur_sum = 0
        for i in range(len(array)):
            if cur_sum <= 0:
                cur_sum = array[i]
            else:
                cur_sum += array[i]

            if cur_sum > max_sum:
                max_sum = cur_sum
        return max_sum


obj = Solution()
# array = [1, -2, 3, 10, -4, 7, 2, -5]
array = [-2, -8, -1, -5, -9]
print(obj.FindGreatestSumOfSubArray(array))
