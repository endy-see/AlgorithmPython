"""
不是基于比较的排序，与被排序的样本的实际数据状况很有关系　所以实际中并不经常使用
桶排序　计数排序:计数排序就是实践了桶排序　基数排序
时间复杂度O(N)
空间复杂的O(N)
"""
import sys


# 给定一个数组 其中存放的所有数（大量）都是在一定范围内的正整数
def BucketSort(arr, n):
    if not arr or len(arr) < 2:
        return
    max_value = sys.maxsize
    for i in range(0, len(arr)):
        max_value = max(max_value, arr[i])
    # 因为一直了数据范围 所以新建一个最大范围的数组
    bucket = [0]*(max_value+1)
    # 遍历arr的每个元素 例如arr[i]=2，则bucket[2]++，即辅助数组上对应的词频加1
    for i in range(0, len(arr)):
        bucket[arr[i]] += 1

    # 输出排序结果
    i = 0
    for j in range(0, len(bucket)):
        while bucket[j] > 0:
            arr[i] = j
            i += 1
            bucket[j] -= 1

