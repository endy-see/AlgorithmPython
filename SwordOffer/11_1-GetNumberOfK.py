"""
题目：数字在排序数组中出现的次数
统计一个数字在排序数组中出现的次数。
例如，输入排序数组{1, 2, 3, 3, 3, 3, 4, 5}和数字3，由于3在这个数组中出现了4次，因此输出4

思路：
既然输入的数组是排序的，那么自然而然地想到用二分查找 但是当用二分找到的3的左边和右边都有3时，
需要左右扫描，时间复杂度O(n)，效率和顺序查找是一样的，面试官不会满意
那么能否用二分查找算法直接找到第一个k及最后一个k呢？
在数组中找到第一个k（get_first_k）：二分找到k，如果k前面的数字不是k，那么此时的中间位置的数字刚好就是第一个k。
如果中间数字的前面一个数字是k，那么第一个k肯定在数组的前半段，下一轮仍然需要在数组的前半段查找
如果未找到k，返回-1
在数组中找到最后一个k（get_last_k）同上类似，二者都是用二分查找算法在数组中查找一个合乎要求的数字
它们的时间复杂度都是O(logn)，因此get_number_of_k的总的时间复杂度是O(logn)
"""


def get_number_of_k(array, k):
    if array and len(array) > 0:
        first_index = get_first_k(array, k, 0, len(array))
        last_index = get_last_k(array, k, 0, len(array))
        if first_index != -1 and last_index != -1:
            return last_index - first_index + 1
    return 0


# 返回第一个k出现的位置（递归）
def get_first_k(array, k, left, right):
    if left > right:
        return -1

    mid = (left + right) >> 1
    if array[mid] > k:
        right = mid - 1
    elif array[mid] < k:
        left = mid + 1
    else:
        if mid > 0 and array[mid-1] != k or mid == 0:
            return mid
        else:
            right = mid - 1
    return get_first_k(array, k, left, right)


# 返回最后一个k出现的位置
def get_last_k(array, k, left, right):
    if left > right:
        return -1

    mid = (left + right) >> 1
    if array[mid] > k:
        right = mid - 1
    elif array[mid] < k:
        left = mid + 1
    else:
        if mid < len(array)-1 and array[mid+1] != k or mid == len(array)-1:
            return mid
        else:
            left = mid + 1
    return get_last_k(array, k, left, right)