"""
题目描述
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

思路：
查找问题 二分查找（只是位置index的变动 这里不需要用递归 用循环就挺好）
注意：需要考虑rotate_array[left]==roate_array[right]==rotate_array[mid]的情况，
遇到左中右三个数字相同的情况是，只能顺序查找了
"""


# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray or len(rotateArray) < 1:
            return 1  # 题意规定
        left = 0
        right = len(rotateArray) - 1
        mid = left
        while rotateArray[left] >= rotateArray[right]:
            if right - left == 1:
                mid = right
                break
            mid = (left + right) >> 1

            # 如果left、right和mid指向的三个数字相同，此时无法确认最小值是位于左边还是右边，只能顺序查找
            if rotateArray[left] == rotateArray[right] and rotateArray[mid] == rotateArray[left]:
                return self.MinInOrder(rotateArray, left, right)

            if rotateArray[mid] >= rotateArray[left]:
                left = mid
            elif rotateArray[mid] <= rotateArray[right]:
                right = mid
        return rotateArray[mid]

    def MinInOrder(self, rotate_array, left, right):
        res = rotate_array[left]
        i = left + 1
        while i <= right:
            if rotate_array[i] < res:
                res = rotate_array[i]
        return res


obj = Solution()
rotate_array = [6501, 6828, 6963, 7036, 7422, 7674, 8146, 8468, 8704, 8717, 9170, 9359, 9719, 9895, 9896, 9913, 9962,
                154, 293, 334, 492, 1323, 1479, 1539, 1727, 1870, 1943, 2383, 2392, 2996, 3282, 3812, 3903, 4465, 4605,
                4665, 4772, 4828, 5142, 5437, 5448, 5668, 5706, 5725, 6300, 6335]
print(obj.minNumberInRotateArray(rotate_array))
