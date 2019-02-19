"""
归并排序

时间复杂度：O(nlogn)
空间复杂度：O(n)  其空间占用主要是临时的数组和递归时压入栈的数据占用：n+logn
稳定排序

思路：
1.先递归分开
2.再逐一合并（注：需要额外辅助数组）

ex: arr=[38, 65, 97, 76, 13, 27, 49]
"""


def MergeSort(arr):
    if not arr or len(arr) < 2:
        return

    merge_sort(arr, 0, len(arr) - 1)


def merge_sort(arr, left, right):
    if left == right:
        return
    mid = int((left + right)/2)
    # mid = (left + right) >> 1
    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)
    merge(arr, left, mid, right)


def merge(arr, left, mid, right):
    # 需要额外辅助数组
    help = [0] * (right - left + 1)
    # 设定3指针变量 分别指向help中待插入的位置和两个待比较、合并的当前位置
    i = 0
    p1 = left
    p2 = mid + 1

    while p1 <= mid and p2 <= right:
        if arr[p1] < arr[p2]:
            help[i] = arr[p1]
            i += 1
            p1 += 1
        else:
            help[i] = arr[p2]
            i += 1
            p2 += 1

    while p1 <= mid:
        help[i] = arr[p1]
        i += 1
        p1 += 1

    while p2 <= right:
        help[i] = arr[p2]
        i += 1
        p2 += 1

    # 用合并后的有序数组help中的数 覆盖arr中对应位置的值
    for i in range(len(help)):
        arr[left + i] = help[i]


arr = [38, 65, 97, 76, 13, 27, 49]
MergeSort(arr)
print(arr)
