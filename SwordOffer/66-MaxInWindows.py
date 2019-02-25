"""
滑动窗口的最大值
题目：给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，
他们的最大值分别为{4,4,6,6,6,5};针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个:
{[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}，
{2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}
思路：双端队列，存放index.左侧放的index始终是当前窗口的最大值，右侧负责动态出入调整
1. 当num[cur] > qmax右侧的最后元素时，
"""

from collections import deque


# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        # size是窗口大小
        if not num or len(num) < 1 or size > len(num) or size <= 0:
            return []

        qmax = deque()
        res = [None] * (len(num) - size + 1)
        index = 0
        for i in range(len(num)):
            # 当前进来的值比队列右侧的index指向的值大时，要不断把比当前小的index弹出
            while qmax and num[qmax[-1]] <= num[i]:
                qmax.pop()
            qmax.append(i)

            # 如果窗口左边缩减 qmax[0]指窗口内最大值
            if qmax[0] == i - size:
                qmax.popleft()

            # 窗口可以开始滑动的时候 只有窗口开始滑动的时候 窗口内最大值才会不断更新
            if i >= size - 1:
                res[index] = num[qmax[0]]
                index += 1
        return res


obj = Solution()
arr = [2, 3, 4, 2, 6, 2, 5, 1]
print(obj.maxInWindows(arr, 3))
