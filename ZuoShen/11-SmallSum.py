"""
小和
题目：在一个数组中，每一个数左边比当前数小的数累加起来，叫做这个数组的小和
     求一个数组的小和
"""


def small_sum(arr):
    if not arr or len(arr) < 2:
        return 0

    return merge_sort(arr, 0, len(arr) - 1)


def merge_sort(arr, left, right):
    if left == right:
        return 0

    mid = (left + right) // 2
    left_sum = merge_sort(arr, left, mid)
    right_sum = merge_sort(arr, mid+1, right)
    merge_sum = merge(arr, left, mid, right)
    return left_sum+right_sum+merge_sum


def merge(arr, left, mid, right):
    help = [0] * (right-left+1)
    i = left
    j = mid+1
    k = 0
    res = 0
    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            res += (right - j + 1)*arr[i]
            help[k] = arr[i]
            i += 1
        else:
            help[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:
        help[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        help[k] = arr[j]
        j += 1
        k += 1

    for i in range(len(help)):
        arr[left+i] = help[i]
    return res

