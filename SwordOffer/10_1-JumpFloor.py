"""
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）
"""


# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number <= 0:
            return 0
        if number == 1:
            return 1

        i = 2
        fn_1 = 1
        fn_2 = 1
        res = 0
        while i <= number:
            res = fn_1 + fn_2
            fn_1 = fn_2
            fn_2 = res
            i += 1
        return res