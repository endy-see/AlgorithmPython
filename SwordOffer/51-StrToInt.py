"""
把字符串转换成整数
题目：将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，
要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。
输入描述：输入一个字符串,包括数字字母符号,可以为空
输出描述：如果是合法的数值表达式则返回该数字，否则返回0
注：
1.正负号
2.溢出
3.字符不合法
ex: 123,
"""


# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        if not s or len(s) < 1:
            return 0

        res = 0
        if '0' <= s[0] <= '9':
            res = int(s[0]) * 10 ** (len(s) - 1)

        if len(s) > 1:
            for i in range(1, len(s)):
                if '0' <= s[i] <= '9':
                    res += int(s[i]) * 10 ** (len(s) - 1 - i)
                else:
                    return 0
        if s[0] == '-':
            return -res
        else:
            return res


obj = Solution()
print(obj.StrToInt('-123'))
