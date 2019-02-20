"""
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
注意：考虑要全面 比如指数为负数的情况，base为0的情况 指数为0的情况
"""


# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        # return math.pow(base, exponent)
        if base == 0:
            return 0

        abs_exponente = abs(exponent)
        res = self.power_with_unsigned_exponent(base, abs_exponente)
        if exponent < 0:
            res = 1/res
        return res

    def power_with_unsigned_exponent(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base

        result = self.power_with_unsigned_exponent(base, exponent >> 1)
        result *= result
        if exponent & 0x1 == 1:
            result *= base
        return result