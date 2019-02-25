"""
1~n整数中1出现的次数
题目：输入一个整数n，求1~n这n个整数的十进制表示中1出现的次数
例如：输入12，1~12这些整数中包含1的数字有1、10、11和12，1一共出现了5次。
思路：
将n的各个位分为两类：个位与其它位。
对个位来说：
若个位大于0，1出现的次数为round*1+1
若个位等于0，1出现的次数为round*1
对其它位来说，记每一位的权值为base，位值为weight，该位之前的数是former，则：
若weight为0，则1出现次数为round*base
若weight为1，则1出现次数为round*base+former+1
若weight大于1，则1出现次数为rount*base+base

比如：
534 = （个位1出现次数）+（十位1出现次数）+（百位1出现次数）=（53*1+1）+（5*10+10）+（0*100+100）= 214
530 = （53*1）+（5*10+10）+（0*100+100） = 213
504 = （50*1+1）+（5*10）+（0*100+100） = 201
514 = （51*1+1）+（5*10+4+1）+（0*100+100） = 207
10 = (1*1)+(0*10+0+1) = 2
时间复杂度为O(logn)
"""


# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n < 1:
            return 0

        count = 0
        base = 1
        round = n
        while round > 0:
            weight = round % 10
            round //= 10
            count += round * base
            if weight == 1:
                count += (n % base) + 1
            elif weight > 1:
                count += base
            base *= 10
        return count
