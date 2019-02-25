"""
和为S的连续正数序列
题目：输入一个正数s，打印出所有和为s的连续正数序列（至少含有两个数）
输出描述：输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
例如，输入15，由于1+2+3+4+5=4+5+6=7+8=15，所以打印出3个连续序列1~5，4~6和7~8
思路：
考虑用两个数small和big分别表示序列的最小值和最大值。首先把small初始化为1，
big初始化为2。如果从small到big的序列的和大于s，则可以从序列中去掉较小值，也就是
增大small；如果从small到big的序列的和小于s，则可以增大big，让这个序列包含更多
的数。因为这个序列至少要两个数，我们一直增加small到(1+s)/2为止
"""


# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum < 3:
            return []

        small = 1
        big = 2
        mid = (1 + tsum) // 2
        cur_sum = small + big
        res = []
        while small < mid:
            if cur_sum == tsum:
                res.append(self.get_sub_sequence(small, big))
            # cur_sum大了，就减小的，直到减到小于等于tsum为止
            while cur_sum > tsum and small < mid:
                cur_sum -= small
                small += 1

                if cur_sum == tsum:
                    res.append(self.get_sub_sequence(small, big))

            big += 1
            cur_sum += big
        return res

    def get_sub_sequence(self, small, big):
        res = []
        for i in range(small, big+1):
            res.append(i)
        return res

obj = Solution()
print(obj.FindContinuousSequence(3))