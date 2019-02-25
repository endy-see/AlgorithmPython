"""
字符串的排列
题目：输入一个字符串，按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc，则打印出由字符串abc、acb、bac、bca、cab和cba
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
思路：
1. 把字符串分成两部分：一部分是字符串的第一个字符；另一部分是第一个
字符以后的所有字符（有阴影背景的区域）。接下来求当前遍历字符之后部分
的字符串的排列
2. 拿第一个字符和它后面的字符逐个交换（注：对python不适用，字符串中的字符无法直接交换）
"""


# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        res = []
        self.permutation(ss, res, '')
        return sorted(list(set(res)))

    def permutation(self, ss, res, path):
        if not ss:
            res.append(path)
        else:
            for i in range(len(ss)):
                # ss[:i]表示字符串ss中，当前字符之前的部分（不含当前字符）
                # ss[i+1:]表示字符串ss中，当前字符之后的部分（不含当前字符）
                self.permutation(ss[:i] + ss[i+1:], res, path + ss[i])


obj = Solution()
print(obj.Permutation('abcdef'))