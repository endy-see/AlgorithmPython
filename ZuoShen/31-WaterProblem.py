"""
题目：以数组大小，来确定装水的问题
这个题目很妙，需要左右两个指针，另外还需要两个变量，一个代表左边的最大值，一个代表右边的最大值
给定一个数组代表一个容器，比如[3, 1, 2, 4]
代表0位置是一个宽度为1， 高度为3的直方图。
代表1位置是一个宽度为1， 高度为1的直方图。
代表2位置是一个宽度为1， 高度为2的直方图。
代表3位置是一个宽度为1， 高度为4的直方图。
所有直方图的底部都在一条水平线上，且紧靠着。
把这个图想象成一个容器， 这个容器可以装3格的水。
给定一个没有负数的数组arr， 返回能装几格水？
"""


def getWater1(arr):
    if not arr or len(arr) < 3:
        return 0
    value = 0
    for i in range(1, len(arr) - 1):
        left_max = 0
        right_max = 0
        for l in range(i):
            left_max = max(arr[l], left_max)
        for r in range(i + 1, len(arr)):
            right_max = max(arr[r], right_max)
        value += max(0, min(left_max, right_max) - arr[i])
    return value


arr = [3, 1, 2, 4]
print(getWater1(arr))

