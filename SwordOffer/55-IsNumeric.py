"""
表示数值的字符串
题目：请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100"，"5e2"，"-123"，"3.1216"和"-1E-16"都表示数值，
但是"12e","1a3.14","1.2.3","+-5""12e+4.3"都不是
原理：表示数值的字符串遵循模式A[.[B]][e|EC] 或者.B[e|EC]
其中A为数值的整数部分，B紧跟着小数点为数值的小数部分，C紧跟着'e'或者'E'，为数值的指数部分。
在小数里可能没有数值的整数部分。例如，小数.123=0.123。因此A部分不是必须的。
如果一个数没有整数部分，那么它的小数部分不能为空
上述A和C都是可能以'+'或'-'开头的0~9的数位串；B也是0~9的数位串，但前面不能有正负号
ex：'123.45e+6'：'123'是整数部分A，'45'是它的小数部分B，'+6'是它的指数部分C
思路：
判断一个字符串是否符合上述模式，首先应尽可能多地扫描0~9的数位（有可能在起始处有'+'或者'-'），
也就是前面模式中表示数值整数的A部分。如果遇到小数点'.'，则开始扫描表示数值小数部分的B部分。
如果遇到'e'或者'E'，则开始扫描表示数值指数的C部分。A、C是整数（可以有正负号，也可以没有）B是无符号整数
"""

# -*- coding:utf-8 -*-
import re


class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        a = re.match(r"[\+-]?[0-9]*(\.[0-9]*)?([eE][\+-]?[0-9]+)?", s)  # [0-9]*:表示至少0个；[0-9]+:表示至少1个
        if a.group(0) == s:
            return True
        else:
            return False
        # return re.match(r"^[\+\-]?[0-9]*(\.[0-9]*)?([eE][\+\-]?[0-9]+)?$",s)

    # s字符串
    def isNumeric1(self, s):
        # write code here
        try:
            p = float(s)
            return True
        except:
            return False

    # s字符串
    def isNumeric(self, s):
        if not len(s):
            return False
        size = len(s)
        if size == 1:
            if '0' <= s[0] <= '9':
                return True
            else:
                return False
        start = 0
        if s[0] == '+' or s[0] == '-':
            start += 1
        for i in range(start, size):
            if '0' <= s[i] <= '9':
                continue
            if s[i] == '.':
                return self.afterDot(s[i + 1:])
            if s[i] == 'e' or s[i] == 'E':
                return self.afterE(s[i + 1:])
            else:
                return False
        return True

    def afterE(self, s):
        """
        no dot or another E/e after E/e in number
        """
        if not len(s):
            return False
        size = len(s)
        start = 0
        if s[0] == '+' or s[0] == '-':
            start += 1
        for i in range(start, size):
            if '0' <= s[i] <= '9':
                continue
            else:
                return False
        return True

    def afterDot(self, s):
        """
        no dot but can have E/e after dot in number
        """
        if not len(s):
            return False
        size = len(s)
        for i in range(size):
            if '0' <= s[i] <= '9':
                continue
            if s[i] == 'e' or s[i] == 'E':
                return self.afterE(s[i + 1:])
            else:
                return False
        return True


obj = Solution()
print(obj.isNumeric('123.e45'))
