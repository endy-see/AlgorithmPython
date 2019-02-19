"""
python中基本的数据结构的使用
栈、队列、堆等
"""

import numpy as np


# 栈：python中的栈其实就是list
def stack_structure():
    stack = [3, 4, 5]
    stack.append(6)
    stack.append(7)
    print(stack)

    print(stack.pop())
    print(stack)


# 双端队列（允许两端都可以进行入队和出队操作的队列）
def queue_structure():
    from collections import deque
    queue = deque(['Eric', 'Jone', 'Michael'])
    queue.append('Terry')  # 右边插入元素
    queue.appendleft('Graham')  # 左边插入元素
    print(queue)
    print(queue.pop())  # pop方法 弹出的是右边的元素
    print(queue.popleft())  # pop方法 弹出的是左边的元素
    print(queue)


# 堆：默认内嵌的heapq模块只支持小根堆
import heapq
def small_heap_structure():
    arr = [38, 65, 97, 76, 13, 27, 49]
    heapq.heappush(arr, 2)          # 向堆中插入元素
    heapq.heappop(arr)              # 从堆中删除元素
    heapq.heapify(arr)              # 将列表转换为堆
    heapq.heapreplace(arr, 11)      # 删除最小元素 添加新元素
    print(heapq.nlargest(2, arr))   # 查询堆中的前n个最大元素
    print(heapq.nsmallest(4, arr))  # 查询堆中的前n个最小元素
    print(arr)


# 堆：大根堆
class BigHeap:
    def __init__(self):
        self.arr = list()

    def heap_insert(self, val):
        heapq.heappush(self.arr, -val)

    def heapify(self):
        heapq.heapify(self.arr)

    def heap_pop(self):
        return -heapq.heappop(self.arr)

    def get_top(self):
        if not self.arr:
            return
        return -self.arr[0]


# 数组（生成固定大小的一维、二维、多维数组或矩阵）
def array_structure():
    # 创建大小为5的一维数组（其实就是列表）
    array_len = 5
    array = [0] * array_len
    print('array', array)

    # 创建大小为2*3的二维矩阵：方法一（推荐）
    m = 2
    n = 3
    matrix2 = [None] * m
    for i in range(len(matrix2)):
        matrix2[i] = [0] * n
    print('matrix2', matrix2)

    # 创建大小为2*3的二维矩阵：方法二
    matrix2_1 = [[0] * n for i in range(m)]
    print('matrix2_1', matrix2_1)

    # 对于创建三维甚至三维以上的数组，建议使用第一种方法，依次确定最高位、次高位及最后一维
    # 如果使用第二种方法，会产生浅拷贝的问题
    k = 4
    matrix3 = [None] * m
    for i in range(len(matrix3)):
        matrix3[i] = [None] * n
    for i in range(len(matrix3)):
        for j in range(len(matrix3[0])):
            matrix3[i][j] = [None] * k
    print('matrix3', matrix3)


# 字符与ASCII码的相互转换
def ascii_structure():
    # 获取字符的ascii码：
    print('字符A的ascii码为：', ord('A'))
    # 获取ascii码对应的字符：
    print('ascii码为97的字符是：', chr(97))
    print('ascii码为97的字符是：', chr(0))
    print('ascii码为97的字符是：', chr(255))


# python常用的排序方法:sort()、sorted()、argsort()
def sort_method():
    # python的内建排序函数有sort、sorted两个
    # 基础的序列升序排序直接调用sorted()方法即可
    ls = list([5, 2, 3, 1, 4])
    new_ls = sorted(ls)
    print(new_ls)
    # 使用ls.sort()也可以，但是它会直接改变ls
    ls.sort()
    print(ls)
    # 注：sort()方法仅定义在list中，无返回值；而sorted()方法对所有的可迭代序列都有效，返回list

    # python3 sorted(iterable, key, reverse)
    # python2 sorted(iterable, cmp, key, reverse)
    ls1 = [('david', 90), ('mary', 90), ('sara', 80), ('lily', 95)]

    # sorted的cmp参数：
    #  sorted(ls1, cmp = lambda x,y: cmp(x[0],y[0])) 按照第一个位置的字母序排序
    #  sorted(ls1, cmp = lambda x,y: cmp(x[1],y[1])) 按照第二个位置的数字序排序

    # sorted的key参数（key的作用：指定一个函数，此函数将在每个元素比较前被调用）：例如通过key指定的函数来忽略字符串的大小写
    # str1 = "This is a test string from Andrew" 有错
    # print(sorted(str1.split(), key=str1.lower()))

    # sorted的reverse参数（由高到低排序）
    print(sorted(ls1, reverse=True))  # 逆转

    # argsort()是numpy库中的函数，它返回的是数组中元素从小到大排序的索引值
    print('一维排序：')
    # 一维数组升序排序和降序排序
    ary1 = np.array([3, 1, 2])
    print(np.argsort(ary1))
    print(np.argsort(-ary1))

    # 二维数组的升序排序和降序排序（多维是0-n指由外到内包裹）
    print('二维排序：')
    ary2 = np.array([[0, 3], [2, 2], [1, 4], [8, 5]])
    print(np.argsort(ary2, axis=0))     # 按行升序排序
    # print(np.argsort(ary2, axis=1))     # 按列升序排序
    print(np.argsort(-ary2, axis=0))    # 按列降序排序1
    # print(np.argsort(-ary2, axis=1))
    print(ary2.argsort(axis=0)[::-1])   # 按列降序排序2：先升序排序 在逆转


# sort_method()
# ascii_structure()
# array_structure()
big_heap_structure()
# small_heap_structure()
# queue_structure()
# stack_structure()
