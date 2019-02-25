"""
圆圈中最后剩下的数字
题目：0,1, ..., n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里面
删除第m个数字。求出这个圆圈里面剩下的最后一个数字
思路：
1.经典解法：用环形链表模拟圆圈
2.创新解法：总结规律 递归求解
  f(n,m) = ｛ 0  n=1;
             [f(n-1,m)+m]%n n>1  n指当前数量
"""


# -*- coding:utf-8 -*-
class Solution:
    # 方法一：构造环形链表
    def LastRemaining_Solution1(self, n, m):
        # write code here
        if n <= 0 or m < 0:
            return -1
        # 将n当做环形链表 删完后直接将该数从n中移除
        count = 0
        index = 0
        next = 0
        array = [0] * n
        for i in range(n):
            array[i] = i
        while len(array) > 1:
            index = next
            count += 1

            if count % m == 0:
                next = index
                array.remove(array[index])
                count = 0
            else:
                next += 1

            if next == len(array):
                next = 0

        return array[0]

    # 方法二：根据递推公式实现
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n <= 0 or m < 0:
            return -1
        if n == 1:
            return 0
        last = 0
        for i in range(2, n+1):
            last = (last + m) % i
        return last


obj = Solution()
print(obj.LastRemaining_Solution(3, 2))
