"""
题目：已知一个整型数组arr，数组长度为size且size大于2，arr有size-1种可以划分成左右两部分的方案
比如：
arr = {3, 2, 3, 4, 1, 2}
第1种划分左部分为[3]，右部分为[2, 3, 4, 1, 2]
第2种划分左部分为[3, 2]，右部分为[3, 4, 1, 2]
第3种划分左部分为[3, 2, 3]，右部分为[4, 1, 2]
第4种划分左部分为[3, 2, 3, 4]，右部分为[1, 2]
第5种划分左部分为[3, 2, 3, 4, 1]，右部分为[2]
每一种划分下，左部分都有最大值记为max_left，右部分都有最大值记为max_right。
求|max_left-max_right|(左部分最大值与右部分最大值之差的绝对值)，最大是多少？
要求：时间复杂度为O(N)，额外空间复杂度O(1)。
"""
import sys


def maxAbs1(arr):
    res = -sys.maxsize
    for i in range(len(arr) - 1):
        max_left = -sys.maxsize
        for j in range(i + 1):
            max_left = max(arr[j], max_left)
        max_right = -sys.maxsize
        for j in range(i + 1, len(arr)):
            max_right = max(arr[j], max_right)
        res = max(abs(max_left - max_right), res)
    return res


def maxAbs2(arr):
    lArr = [0] * len(arr)
    rArr = [0] * len(arr)
    lArr[0] = arr[0]
    rArr[-1] = arr[-1]
    for i in range(1, len(arr)):
        lArr[i] = max(lArr[i-1], arr[i])
    for i in range(len(arr)-2, -1, -1):
        rArr[i] = max(rArr[i+1], arr[i])
    max_res = 0
    for i in range(len(arr)-1):
        max_res = max(max_res, abs(lArr[i]-rArr[i+1]))
    return max_res


def maxAbs3(arr):
    max_res = -sys.maxsize
    for i in range(len(arr)):
        max_res = max(arr[i], max_res)
    return max_res - min(arr[0], arr[-1])


arr = [3, 2, 3, 4, 1, 2]
print(maxAbs1(arr))
print(maxAbs2(arr))
print(maxAbs3(arr))
