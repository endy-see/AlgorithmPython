"""
翻转单词顺序
题目：输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，
标点符号和普通字母一样处理。例如输入字符串"I am a student."，则输出"student. a am i"
"""


# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if not s or len(s) < 1:
            return s
        str_array = s.split(' ')
        left = 0
        right = len(str_array) - 1
        while left < right:
            tmp = str_array[left]
            str_array[left] = str_array[right]
            str_array[right] = tmp
            left += 1
            right -= 1
        return ' '.join(str_array)


obj = Solution()
s = 'I am a student.'
print(obj.ReverseSentence(s))
