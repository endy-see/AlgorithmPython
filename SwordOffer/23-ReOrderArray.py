"""
调整数组顺序使奇数位于偶数前面
题目：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数
位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数
之间的相对位置不变
思想：由于要保持相对位置不变，所以在partition过程中，只能每次把偶数部分往后移
而不能随意交换（相当于用了插入排序的思想）
"""


# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        if not array or len(array) < 1:
            return array
        self.partition(array)
        return array

    def partition(self, arr):
        left = -1
        for i in range(0, len(arr)):
            # 只有当i-left>1时二者间才有空位
            if arr[i] % 2 == 1:
                if i-left > 1:
                    cur_odd = arr[i]
                    # 把left到i之间的偶数右移1位 再把arr[i]插入到空位
                    for j in range(i, left+1, -1):
                        arr[j] = arr[j-1]
                    arr[left+1] = cur_odd
                left += 1


obj = Solution()
arr = [1, 2, 3, 4, 5, 6]
print(obj.reOrderArray(arr))




