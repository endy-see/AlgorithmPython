"""
数字在排序数组中出现的次数
题目：统计一个数字在排序数组中出现的次数
思路：看到有序，使用二分查找
使用二分找到这段连续k的最左边的位置，最右边的位置，两个相减+1就是长度了
ex: [1, 2, 3, 3, 4, 5, 6, 7, 7, 7, 8], [1, 3, 3, 3, 3, 4, 5]
"""


# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if not data or len(data) < 1 or k < data[0] or k > data[-1]:
            return 0
        num = 0
        first = self.get_first_k(data, k, 0, len(data) - 1)
        last = self.get_last_k(data, k, 0, len(data) - 1)
        if first > -1 and last > -1:
            num = last - first + 1
        return num

    # 在arr中找到k第一次出现的位置
    def get_first_k(self, arr, k, left, right):
        if left == right:
            if arr[left] == k:
                return left
            else:
                return -1

        mid = (left + right) // 2
        if arr[mid] > k:
            right = mid - 1
        elif arr[mid] < k:
            left = mid + 1
        else:
            if mid == 0 or arr[mid - 1] != k:
                return mid
            else:
                right = mid - 1
        return self.get_first_k(arr, k, left, right)

    def get_last_k(self, arr, k, left, right):
        if left == right:
            if arr[left] == k:
                return right
            else:
                return -1
        mid = (left + right) // 2
        if arr[mid] > k:
            right = mid - 1
        elif arr[mid] < k:
            left = mid + 1
        else:
            if mid == right or arr[mid + 1] != k:
                return mid
            else:
                left = mid + 1
        return self.get_last_k(arr, k, left, right)


obj = Solution()
# arr = [1, 2, 3, 3, 4, 5, 6, 7, 7, 7, 8]
arr = [1, 3, 3, 3, 3, 4, 5]
print(obj.GetNumberOfK(arr, 2))
