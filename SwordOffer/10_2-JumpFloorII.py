"""
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

思路：
f(0)=1 表示一步一次性登到n>1的台阶时的一种方法
f(1)=1
f(2)=2=f(1)+f(0)
f(3)=4=f(2)+f(1)+f(0)
...
f(n)=2^(n-1)=f(n-1)+f(n-2)+...+f(2)+f(1)+f(0)
"""


# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number < 1:
            return 0
        return pow(2, number - 1)

