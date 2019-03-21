"""
BFPRT算法：在一个无序数组中找到第k小的数（或在一个无序数组中找到第kda的数）
方法一：比较优良的解法：快排的partition过程 时间复杂度最大O(N^2) 最小O(N)，平均时间复杂度是O(N)，但是有随机成分
方法二：同样是用快排的partition，但是选择的target有讲究（中位数），不再是随机选了
"""


def get_mink_nums_by_bfprt(arr, k):
    if not arr or len(arr) < 1 or k < 0 or len(arr) < k:
        return None
    copy_arr = copyArr(arr)
    return select(copy_arr, 0, len(arr) - 1, k - 1)


def select(arr, left, right, k):
    if left == right:
        return arr[left]
    target = median_of_medians(arr, left, right)
    small_big = partition(arr, left, right, target)
    if small_big[0] <= k <= small_big[1]:
        return arr[k]
    elif k < small_big[0]:
        return select(arr, left, small_big[0] - 1, k)
    else:
        return select(arr, small_big[1] + 1, right, k)


def median_of_medians(arr, left, right):
    num = right - left + 1
    offset = 0 if num % 5 == 0 else 1
    mArr = [0] * (num // 5 + offset)
    for i in range(len(mArr)):
        beginI = left + i * 5
        endI = beginI + 4
        mArr[i] = get_median(arr, beginI, min(right, endI))
    return select(mArr, 0, len(mArr) - 1, len(mArr) // 2)


def partition(arr, left, right, target):
    small = left - 1
    big = right + 1
    cur = left
    while cur < big:
        if arr[cur] < target:
            swap(arr, cur, small+1)
            small += 1
            cur += 1
        elif arr[cur] > target:
            swap(arr, cur, big-1)
            big -= 1
        else:
            cur += 1
    return [small+1, big-1]


def get_median(arr, begin, end):
    insertion_sort(arr, begin, end)
    sum = end + begin
    mid = sum // 2 + sum % 2
    return arr[mid]


def insertion_sort(arr, begin, end):
    for i in range(begin + 1, end + 1):
        for j in range(i, begin, -1):
            if arr[j - 1] > arr[j]:
                swap(arr, j - 1, j)
            else:
                break


def swap(arr, i1, i2):
    tmp = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = tmp


def copyArr(arr):
    res = [0] * len(arr)
    for i in range(len(arr)):
        res[i] = arr[i]
    return res


if __name__ == '__main__':
    arr = [6, 9, 1, 3, 1, 2, 2, 5, 6, 1, 3, 5, 9, 7, 2, 5, 6, 1, 9]
    res = sorted(arr)
    print(get_mink_nums_by_bfprt(arr, 10))

