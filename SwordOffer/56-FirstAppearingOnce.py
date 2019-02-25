"""
字符流中第一个不重复的字符
题目：请实现一个函数用来找出字符流中第一个只出现一次的字符。
例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
输入描述：如果当前字符流没有存在出现一次的字符，返回#字符
注：
1. 由于要求的是第一个，所以不能只用dict，因为dict不保证顺序，但是可以记录每次字符流组成的字符串，从前往后遍历找到第一个就行；
2. 可以尝试使用collections.OrderedDict
3. 固定长度的数组
"""

from collections import OrderedDict
# -*- coding:utf-8 -*-
class Solution:
    def __init__1(self):
        self.s = ''
        self.dict = {}

    # 返回对应char
    def FirstAppearingOnce1(self):
        # write code here
        if not self.s:
            return '#'
        for char in self.s:
            if self.dict[char] == 1:
                return char
        return '#'

    def Insert1(self, char):
        # write code here
        if char:
            self.s += char
            if char in self.dict:
                self.dict[char] += 1
            else:
                self.dict[char] = 1

    def __init__(self):
        self.ordered_dict = OrderedDict()

    def FirstAppearingOnce(self):
        for k, v in self.ordered_dict.items():
            if v == 1:
                return k
        return '#'

    def Insert(self, char):
        if char:
            if char in self.ordered_dict:
                self.ordered_dict[char] += 1
            else:
                self.ordered_dict[char] = 1


obj = Solution()
obj.Insert('g')
print(obj.FirstAppearingOnce())
