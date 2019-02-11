"""
题目描述
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

思路：
f(1)=1
f(2)=2
f(3)=f(2)+f(1)
...
f(n)=f(n-1)+f(n-2)
"""


# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, n):
        # write code here
        if n < 1:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        i = 3
        fn_1 = 1
        fn_2 = 2
        while i <= n:
            res = fn_1 + fn_2
            fn_1 = fn_2
            fn_2 = res
            i += 1
        return res


