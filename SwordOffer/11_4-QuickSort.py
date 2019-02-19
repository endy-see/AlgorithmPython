"""
快速排序（递归）

平均时间复杂度：O(nlogn)   最好情况O(nlogn) 最坏情况O(n^2)
空间复杂度：最好情况O(logn)，即每一次都平分数组；最坏情况O(n)，即退化为冒泡排序的情况
不稳定排序

思路：
1.patition过程：荷兰国旗问题
2.随机选定anchor: random.random()随机生成一个[0,1)范围内的实数
"""

import random


# 由于待排序时的数组中有可能存在与anchor相等的值，
# 所以这里的partition过程会把数组分成3个部分：
# 小于anchor的部分、等于anchor的部分和大于anchor的部分
def partition(arr, left, right, anchor):
    # 用两个变量small和big分别卡住小于anchor的位置和大于anchor的位置
    small = left - 1
    big = right + 1
    cur = left

    while cur != big:
        if arr[cur] < anchor:
            swap(arr, small+1, cur)
            small += 1
            cur += 1
        elif arr[cur] > anchor:
            swap(arr, big-1, cur)
            big -= 1
        else:
            cur += 1

    return [small, big]


def QuickSort(arr):
    if not arr or len(arr) < 2:
        return

    partition_sort(arr, 0, len(arr) - 1)


def partition_sort(arr, left, right):
    if left >= right:
        return

    # 注释掉下面两行，就是经典快排
    anchor_index = int(random.random() * (right - left + 1) + left)
    swap(arr, right, anchor_index)

    small_big = partition(arr, left, right-1, arr[right])
    # 注意把最后一个数与big位置的数交换
    swap(arr, right, small_big[1])
    partition_sort(arr, left, small_big[0])
    partition_sort(arr, small_big[1]+1, right)


def swap(arr, index1, index2):
    tmp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = tmp


# 练习：给定anchor，将数组中大于等于anchor的数放在左边，小于anchor的数放在右边
def partition1(arr, anchor):
    if not arr or len(arr) < 1:
        return

    # 用一个变量small_eq记录小于等于anchor的左边部分
    small_eq = -1
    cur = 0
    while cur < len(arr):
        if arr[cur] <= anchor:
            # 将small的下个位置的值与cur位置的值交换
            swap(arr, small_eq+1, cur)
            small_eq += 1
        cur += 1
        # 从前面换到cur位置的值由于大小位置 还是需要继续做判断的


# 随机快排
arr = [7, 3, 2, 10, 8, 15, 3, 5, 7, 5, 6, 9, 5, 3, 5]
# arr = [8, 6, 2, 9, 13, 0, 15, 11, 3, 22]
# QuickSort(arr)
# print(arr)

# 测试partition2
partition1(arr, 5)
print(arr)
