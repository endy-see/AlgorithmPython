"""
python中基本的数据结构的使用
栈、队列、堆等
"""


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


ascii_structure()
# array_structure()
# queue_structure()
# stack_structure()
