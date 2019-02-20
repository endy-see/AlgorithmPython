"""
数组中只出现一次的(两个)数字
题目：一个整型数组里除两个数字之外，其他数字都出现了两次。
请写程序找出这两个只出现一次的数字。
要求：时间复杂度O(n)，空间复杂度O(1)
ex: [2, 4, 3, 6, 3, 2, 5, 5]
"""


# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if not array or len(array) < 2:
            return []
        xor = array[0]
        for i in range(1, len(array)):
            xor ^= array[i]
        # 从右向左找到第一个不为0的位
        num_1 = 1
        for i in range(0, 32):
            if num_1 & xor != 0:
                break
            num_1 <<= 1

        index_of_1_is1 = []
        index_of_1_not1 = []
        for i in range(0, len(array)):
            if array[i] & num_1 != 0:
                index_of_1_is1.append(array[i])
            else:
                index_of_1_not1.append(array[i])

        res1 = index_of_1_is1[0]
        for i in range(1, len(index_of_1_is1)):
            res1 ^= index_of_1_is1[i]

        res2 = index_of_1_not1[0]
        for i in range(1, len(index_of_1_not1)):
            res2 ^= index_of_1_not1[i]

        return [res1, res2]


obj = Solution()
array = [2, 4, 3, 6, 3, 2, 5, 5]
print(obj.FindNumsAppearOnce(array))
