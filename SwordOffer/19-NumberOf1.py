"""
二进制中1的个数
题目：输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
注意：负数
"""


# -*- coding:utf-8 -*-
class Solution:
    # 方法一：首先把n和1做与运算，判断n的最低位是否为1.然后把1依次左移，不断判断n的某位上是否为1
    # 确定：循环的次数等于整数二进制的位数，32位的整数需要循环32次
    def NumberOf1(self, n):
        # write code here
        num_of_1 = 0
        bit_1_move = 1
        for i in range(0, 32):
            if n & bit_1_move != 0:
                num_of_1 += 1
            bit_1_move <<= 1
        return num_of_1

    # 方法二：整数中有几个1就只需要循环几次
    # 把一个整数减去1，再和原整数做与运算，会把该整数最右边的1变成0.
    # 那么一个整数的二进制表示中有多少个1，就可以进行多少次这样的操作。
    def NumberOf12(self, n):
        num_of_1 = 0
        while n != 0 and n >= -2147483648:
            num_of_1 += 1
            n = n & (n - 1)
        return num_of_1


obj = Solution()
# print(obj.NumberOf12(10))
print(obj.NumberOf12(-1))
