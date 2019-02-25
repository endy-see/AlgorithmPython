"""
构建乘积数组
题目：
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素
B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法
法1：直接连乘n-1个数，得到B[i]；时间复杂度：O(n^2)
法2：构建前向乘积数组C[i]=A[0]*A[1]*...*A[i-1]，即C[i]=C[i-1]*A[i-1]；
构建后向乘积数组D[i]=A[n-1]*A[n-2]*...A[n-i+1]，即D[i]=D[i+1]*A[i+1]；
通过C[i],D[i]来求B[i]：B[i]=C[i]*D[i]；时间复杂度：O(n)
"""


# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        if not A or len(A) < 2:
            return A
        B = [None] * len(A)
        B[0] = 1
        for i in range(1, len(A)):
            B[i] = B[i-1] * A[i-1]
        tmp = 1
        # 因为最右边的数是不需要再右边的数来累乘的，所以从lenA-2（倒数第二个数）开始
        for i in range(len(A)-2, -1, -1):
            tmp *= A[i+1]
            B[i] *= tmp
        return B


obj = Solution()
A = [1, 2, 3, 4, 5, 6, 7]
print(obj.multiply(A))