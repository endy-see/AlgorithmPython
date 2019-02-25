"""
丑数
题目：把只包含因子2，3和5的数称作丑数（ugly number）。例如6、8都是丑数，但14不是，
因为它包含质因子7。习惯上我们把1当做第一个丑数。求按从小到大的顺序的第N丑数。
思路：两种方法
法1. 逐个判断每个整数是不是丑数（连续除以2、连续除以3、连续除以5） 直观但不高效
法2. 创建数组保存已经找到的丑数，用空间换时间的解法
"""


# -*- coding:utf-8 -*-
class Solution:
    # 方法一：逐个判断每个整数是不是丑数
    def GetUglyNumber_Solution1(self, index):
        if index < 1:
            return 0

        ugly_count = 0
        i = 0
        while ugly_count < index:
            i += 1
            if self.is_ugly(i):
                ugly_count += 1

        return i

    def is_ugly(self, num):
        while num % 2 == 0:
            num //= 2
        while num % 3 == 0:
            num //= 3
        while num % 5 == 0:
            num //= 5

        if num == 1:
            return True
        else:
            return False

    # 方法二：空间换时间
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index < 1:
            return 0
        help = [None] * index
        help[0] = 1
        cur2_index = 0
        cur3_index = 0
        cur5_index = 0
        for i in range(index-1):
            help[i+1] = min([help[cur2_index] * 2, help[cur3_index] * 3, help[cur5_index] * 5])
            # 每一次改变都是为了超越
            while help[cur2_index]*2 <= help[i+1]:
                cur2_index += 1
            while help[cur3_index]*3 <= help[i+1]:
                cur3_index += 1
            while help[cur5_index]*5 <= help[i+1]:
                cur5_index += 1
        return help[-1]


obj = Solution()
print(obj.GetUglyNumber_Solution(100))
