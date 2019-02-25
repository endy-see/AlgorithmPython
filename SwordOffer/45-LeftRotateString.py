"""
左旋转字符串
题目：字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"
和数字2，该函数返回左旋转两位得到的结果"cdefgab"
思路：
1. 先将s[:k]和s[k:]内部各字符互相交换
2. 再将s中所有字符，左右互相交换
"""


# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if not s or len(s) < 1 or n > len(s):
            return ''
        char_array = list(s)
        self.swap(char_array, 0, n-1)
        self.swap(char_array, n, len(char_array)-1)
        self.swap(char_array, 0, len(char_array)-1)
        return ''.join(char_array)

    def swap(self, array, i, j):
        while i < j:
            tmp = array[i]
            array[i] = array[j]
            array[j] = tmp
            i += 1
            j -= 1


obj = Solution()
print(obj.LeftRotateString('cdefgab', 2))
