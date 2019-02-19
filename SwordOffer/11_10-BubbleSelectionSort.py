"""
冒泡排序和选择排序
冒泡排序：
法一：将较大的数往后不断交换（相当于大数往后冒泡）
法二：将较小的数往前不断交换（相当于小数往前冒泡）
可以做到稳定
选择排序
法一、每遍历一次数组，获取该轮遍历的最大值，并将其与最后位置的元素互换可以实现从小到大的排序
法二：每遍历一次数组，获取该轮遍历的最小值，并将其前面位置的元素互换也可以实现从小到大的排序结果
做不到稳定（相同的数相对顺序不变）
"""


# 冒泡1：不断将较大的数往后交换
def BubbleSort1(arr):
    if not arr or len(arr) < 1:
        return
    # 默认第一层循环是从后向前表示已经排好的数字
    for i in range(len(arr)-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)


# 冒泡2：不断将较小的数往前交换
def BubbleSort2(arr):
    if not arr or len(arr) < 1:
        return
    # 默认第一层循环是才能够前往后表示已经排好的数字
    for i in range(0, len(arr)):
        for j in range(len(arr)-1, i, -1):
            if arr[j] < arr[j-1]:
                swap(arr, j, j-1)


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


#  选择1：每次遍历选择一个最大数与后面待排序的元素交换，从而使得从后向前、从大到小变得有序
def SelectionSort1(arr):
    if not arr or len(arr) < 1:
        return
    for i in range(len(arr)-1, 0, -1):
        max_index = i
        max_value = arr[i]
        for j in range(0, i):
            # 从j到i遍历，如果遇到比arr[i]大的元素，则记录较大值及其index
            if arr[j] > max_value:
                max_index = j
                max_value = arr[j]
        if max_index != i:
            arr[max_index] = arr[i]
            arr[i] = max_value


#  选择2：每次遍历选择一个最小数与前面待排序的元素交换，从而使得从前向后、从小到大变得有序
def SelectionSort2(arr):
    if not arr or len(arr) < 1:
        return
    for i in range(0, len(arr)-1):
        min_index = i
        min_value = arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] < min_value:
                min_index = j
                min_value = arr[j]
        if i != min_index:
            arr[min_index] = arr[i]
            arr[i] = min_value


arr = [38, 65, 97, 76, 13, 27, 49]
SelectionSort2(arr)
print(arr)