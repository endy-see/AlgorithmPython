"""
把数组排成最小的数
题目：
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
思路：
先将整数数组转为字符串数组，然后用比较器实现字符串比较大小。
如果有字符串A和B， A + B < B + A，则A在前；
反之B在前。最后将字符串数组连接去除返回值左侧的0。
两种方法，分别针对python2和python3
"""


# -*- coding:utf-8 -*-
class Solution:
    # python3
    def PrintMinNumber1(self, numbers):
        if numbers is None or len(numbers) < 1:
            return ""
        numbers = list(map(str, numbers))
        # 先对numbers中的字符串进行两两全排列
        res = []
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                pre = numbers[i] + numbers[j]
                last = numbers[j] + numbers[i]
                # 比较组合之后的ab和ba
                if self.compare(pre, last) > 0:
                    # 说明last<pre 需要交换
                    self.swap(numbers, i, j)
            res.append(numbers[i])
        return ''.join(numbers).lstrip()

    def compare(self, str1, str2):
        if str1 > str2:
            return 1
        else:
            return 0

    def PrintMinNumber(self, numbers):
        if numbers is None or len(numbers) < 1:
            return ""
        numbers = list(map(str, numbers))
        # 先对numbers中的字符串进行两两全排列
        res = []
        for i in range(len(numbers) - 1, 0, -1):
            for j in range(i):
                # 比较组合之后的ab和ba
                if numbers[j] + numbers[j + 1] > numbers[j + 1] + numbers[j]:
                    # 说明last<pre 需要交换
                    self.swap(numbers, j, j + 1)
        return ''.join(numbers).lstrip()

    def swap(self, arr, i, j):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp


obj = Solution()
# array = [3, 32, 321]
array = [3, 5, 1, 4, 2]
print(obj.PrintMinNumber(array))
