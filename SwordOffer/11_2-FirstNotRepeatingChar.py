"""
题目描述
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,
并返回它的位置, 如果没有则返回 -1（需要区分大小写）.

思路：哈希（字典）查找 也可以用长度为256的数组来代替（char是由8位的），这样额外空间复杂度为O(1)
"""


# -*- coding:utf-8 -*-
class Solution:
    # 方法一：用字典实现
    def FirstNotRepeatingChar1(self, s):
        # write code here
        if not s or len(s) < 1:
            return -1

        dict = {}
        for sub_char in s:
            if sub_char in dict:
                dict[sub_char] += 1
            else:
                dict[sub_char] = 1
        for sub_char in s:
            if dict[sub_char] == 1:
                return s.index(sub_char)
        return None

    # 方法二：用数组实现（本题目中限制了字符指字母）
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s or len(s) < 1:
            return -1

        array = [0] * 256
        for sub_char in s:
            array[ord(sub_char)] += 1
        for sub_char in s:
            if array[ord(sub_char)] == 1:
                return s.index(sub_char)
        return -1


obj = Solution()
print(obj.FirstNotRepeatingChar('google'))
