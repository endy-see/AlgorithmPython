"""
正则表达式
请实现一个函数用了匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它
前面的字符可以出现任意次（包含0次）。在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
思路：
1. 先做有效性判断：分别判断字符串和模式是否有效
2. 当模式中的第二个字符不是'*'时，问题要简单很多。如果字符串中的第一个字符和模式中的第一个字符相匹配，
那么在字符串和模式上都向后移动一个字符，然后匹配剩余的字符串和模式。如果字符串中的第一个字符和模式
中的第一个字符不相匹配，则直接返回False
3. 当模式中的第二个字符是'*'时，问题要复杂一些，因为可能有多种不同的匹配方式。一种选择是在模式上向后
移动两个字符。这相当于'*'和它前面的字符被忽略了，因为'*'可以匹配字符串中的0个字符。如果模式中的
第一个字符和字符串中的第一个字符相匹配，则在字符串上向后移动一个字符，而在模式上有两种选择：
可以在模式上向后移动两个字符，也可以保持模式不变
"""


# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if len(s) == 0 and len(pattern) == 0:
            return True
        if len(s) > 0 and len(pattern) == 0:
            return False
        if not self.is_valid(s, pattern):
            return False
        return self.process(s, pattern, 0, 0)

    # 有效性判断
    def is_valid(self, s, pattern):
        for i in range(len(s)):
            if s[i] == '*' or s[i] == '.':
                return False

        for i in range(len(pattern)):
            if pattern[i] == '*' and (i == 0 or pattern[i - 1] == '*'):
                return False
        return True

    def process(self, s, exp, si, ei):
        if ei == len(exp):
            return si == len(s)

        # 第二个字符不是'*'时，如果第一个字符匹配，则字符串和模式同时右移一位，否则直接返回False
        if ei + 1 == len(exp) or exp[ei + 1] != '*':
            return si != len(s) and (exp[ei] == s[si] or exp[ei] == '.') \
                   and self.process(s, exp, si + 1, ei + 1)

        # 第二个字符是'*'时，如果模式中的第一个字符和字符串中的第一个字符相匹配，则在字符串上向后移动一个字符
        # 而模式上有两种选择：可以在模式上向后移动两个字符，也可以保持不变
        while si != len(s) and (exp[ei] == s[si] or exp[ei] == '.'):
            # 如果当前字符串的字符能够和exp[ei+2:]匹配上 就直接返回了 否则字符串上指针不断后移
            # 模式上向后移动两个字符
            if self.process(s, exp, si, ei + 2):
                return True
            # 模式上保持不变
            si += 1

        # exp[ei+1]='*' & exp[ei] != s[si] & exp[ei] != '.' 则直接跳过当前字符及后面的'*'，继续匹配
        return self.process(s, exp, si, ei + 2)


obj = Solution()
# print(obj.match('', '.'))
print(obj.match('', '.*'))

