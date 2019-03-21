"""
最大间隙问题
题目：给定一个无序数组（数组中所有元素都是非负整数），找到数组有序时的连续两个元素间的最大间隙（差值）
要求：线性时间、空间复杂度（即在不排序的情况直接找出数组有序时的最大间隙）
思路：桶排序
1. 找到n个数据中最大值和最小值
2. 用n-2个点等分区间[min, max]，即将[min, max]等分为n-1个区间（前闭后开）
   将这些区间看做桶，编号为1，2，...，n-2,n-1，且桶i的上界和桶i+1的下界相同，即每个桶的大小相同
   每个桶的大小：bucket_size = (max-min)/(n-1)
   除最大最小数据max和min以外的n-2个数据被放入n-1个桶中，所以只好有一个桶是空的
   又因为每个桶的大小相同，所以最大间隙不会出现在同一个桶中
   一定是某个桶的上界和其后桶的下界之间的间隙
"""

import sys


def maximumGap(nums):
    if not nums or len(nums) < 2:
        return 0

    lenth = len(nums)
    min_value = sys.maxsize
    max_value = -sys.maxsize
    for i in range(lenth):
        min_value = min(nums[i], min_value)
        max_value = max(nums[i], max_value)

    if min_value == max_value:
        return 0

    has_num = [False] * (lenth + 1)
    maxs = [0] * (lenth + 1)
    mins = [0] * (lenth + 1)
    for i in range(len(nums)):
        bid = bucket(nums[i], lenth, min_value, max_value)
        mins[bid] = min(mins[bid], nums[i]) if has_num[bid] else nums[i]
        maxs[bid] = max(maxs[bid], nums[i]) if has_num[bid] else nums[i]
        has_num[bid] = True

    res = 0
    last_max = maxs[0]
    for i in range(1, lenth + 1):
        if has_num[i]:
            res = max(res, mins[i] - last_max)
            last_max = maxs[i]
    return res


def bucket(num, lenth, min_value, max_value):
    return int((num - min_value) * lenth / (max_value - min_value))


if __name__ == '__main__':
    arr = [3, 6, 9, 1]
    print(maximumGap(arr))
