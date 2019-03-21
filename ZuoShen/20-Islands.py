"""
岛问题
题目：一个矩阵中只有0和1两种值，每个位置都可以和自己的上、下、左、右四个位置相连，
如果有一片1连在一起，这个部分叫做一个岛，求一个矩阵中有多少个岛？
举例：
001010
111010
100100
000000
这个矩阵中有三个岛
"""


def countIslands(m):
    if not m or not m[0]:
        return 0

    rows = len(m)
    cols = len(m[0])
    res = 0
    for i in range(rows):
        for j in range(cols):
            if m[i][j] == 1:
                res += 1
                infect(m, i, j, rows, cols)

    return res


def infect(m, i, j, rows, cols):
    if i < 0 or i >= rows or j < 0 or j >= cols or m[i][j] != 1:
        return

    m[i][j] = 2
    infect(m, i + 1, j, rows, cols)
    infect(m, i - 1, j, rows, cols)
    infect(m, i, j + 1, rows, cols)
    infect(m, i, j - 1, rows, cols)


if __name__ == '__main__':
    m = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 1, 1, 0, 1, 1, 1, 0],
         [0, 1, 1, 1, 0, 0, 0, 1, 0],
         [0, 1, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 1, 0, 0],
         [0, 0, 0, 0, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    print(countIslands(m))

