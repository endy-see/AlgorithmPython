"""
岛问题：
一个矩阵中只有０和１两种值，每个位置都可以和自己的上下左右四个位置相连
如果一片１连在一起，这个部分叫做一个岛，求一个矩阵中有多少个岛？
举例：
0 0 1 0 1 0
1 1 1 0 1 0
1 0 0 1 0 0
0 0 0 0 0 0
这个矩阵中有三个岛
思想：感染函数　
"""


def get_island_num(arr):
    if arr is None or arr[0] is None:
        return
    m = len(arr)
    n = len(arr[0])
    island_num = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1:
                # 通过感染函数　将当前位置周围的１全部感染成２　避免下次再遍历
                infect(arr, i, j, m, n)
                island_num = island_num + 1
    return island_num


def infect(arr, i, j, m, n):
    # 当前值位置越界或者当前值不等于１　就终止递归
    if i < 0 or i >= m or j < 0 or j >= n or arr[i][j] != 1:
        return
    arr[i][j] = 2
    # 感染下边
    infect(arr, i+1, j, m, n)
    # 感染上边
    infect(arr, i-1, j, m, n)
    # 感染左边
    infect(arr, i, j-1, m, n)
    # 感染右边
    infect(arr, i, j+1, m, n)


if __name__ == '__main__':
    arr1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0, 0, 0, 1, 0],
            [0, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    print(get_island_num(arr1))
    m2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 1, 1, 1, 0, 0, 0, 1, 0],
          [0, 1, 1, 0, 0, 0, 1, 1, 0],
          [0, 0, 0, 0, 0, 1, 1, 0, 0],
          [0, 0, 0, 0, 1, 1, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    print(get_island_num(m2))