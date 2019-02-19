"""
插入排序
思想：
假定从前往后是有序的，从前面已排好序的数组中找到第一个小于等于当前元素值的位置，
然后将该位置后的所有元素右移一位（腾出一个空位），最后将当前元素插入到腾出的空位上即可
可以做到稳定
"""


def InsertSort(arr):
    if not arr or len(arr) < 1:
        return

    for i in range(1, len(arr)):
        # 先用变量保存下当前遍历到的元素位置和值
        cur_index = i
        cur_value = arr[i]
        # 下面就需要把k~j-1之间的元素挪到k+1~j，然后cur_value赋值给arr[k]
        while cur_index > 0 and arr[cur_index - 1] > cur_value:
            arr[cur_index] = arr[cur_index - 1]
            cur_index -= 1
        # 只有当发生了后移（cur_index变化了）的时候，才需要当前值去填充
        # 如果cur_index没有变化，说明cur_index前一个位置的值比cur_index位置的值小了，故不需要挪动
        if cur_index != i:
            arr[cur_index] = cur_value


arr = [38, 65, 97, 76, 13, 27, 49]
InsertSort(arr)
print(arr)
