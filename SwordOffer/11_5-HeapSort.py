"""
堆排序

概念：堆其实就是一棵完全二叉树（若设二叉树的深度为h，除第 h 层外，
其它各层 (1～h-1) 的结点数都达到最大个数，第 h 层所有的结点都连续集中在最左边）

时间复杂度：O(nlogn)
空间复杂度：O(1)（没有像快排那样使用递归，就地排序）
不稳定排序

思路：堆排包括两个步骤
1.heap_insert: 构建堆的过程（这里由小到大排序，构建的是大根堆）
2.heapify: 调整堆的过程：每次将堆顶元素与数组最后一个元素交换

ex: arr=[38, 65, 97, 76, 13, 27, 49]
"""


def HeapSort(arr):
    if not arr or len(arr) < 2:
        return

    # 先构建大根堆
    for i in range(1, len(arr)):
        heap_insert(arr, i)

    # 将对顶元素与最后一个位置的元素交换
    swap(arr, 0, len(arr)-1)

    # 再调整大根堆（堆的大小逐渐从len(arr)-2递减）
    for i in range(len(arr)-2, 0, -1):
        heapify(arr, 0, i)
        swap(arr, 0, i)


# 循环与父节点比较，如果比父值大，则交换
# 堆中i位置的父：(i-1)/2
# 堆中i位置的左孩子：2*i+1, 2*i+2
def heap_insert(arr, index):
    while index > 0:
        parent_index = int((index - 1)/2)
        if arr[index] > arr[parent_index]:
            swap(arr, index, parent_index)
            # 这里是一个循环赋值　即不断往上找父节点　父节点的父节点　
            # 直到找到第一个比value大的父时停止与父的交换
            index = parent_index
        else:
            break


# 在left到right范围上调整堆（在本例中，left始终是从0开始，但是为了更加通用，这里还是留出了left变量）
def heapify(arr, left, right):
    # 将cur位置的节点与其左、右孩子比较，并与左右孩子中较大的值交换
    # 如果没有左右孩子的值均小于cur位置的值，break
    left_child_index = 2*left + 1
    right_child_index = 2*left + 2
    max_index = left

    while left_child_index < right:
        if arr[left_child_index] > arr[max_index]:
            max_index = left_child_index
        if right_child_index < right and arr[right_child_index] > arr[max_index]:
            max_index = right_child_index
        if max_index != left:
            swap(arr, left, max_index)
        else:
            break

        left = max_index
        left_child_index = 2*left + 1
        right_child_index = 2*left + 2


def swap(arr, index1, index2):
    tmp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = tmp


arr = [38, 65, 97, 76, 13, 27, 49]
HeapSort(arr)
print(arr)