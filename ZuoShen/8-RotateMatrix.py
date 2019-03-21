"""
旋转正方形矩阵90
题目：给定一个整型正方形矩阵matrix，请把该矩阵调整成顺时针旋转90度的样子
要求额外空间复杂度为O(1)
思路：只要保证边界上的位置变化不乱，那么里面的元素位置也不会乱
要打印一个点，需要找到其他的三个点进行位置的变化
"""


def rotate_matrix(m):
    if not m or len(m) < 1 or not m[0] or len(m[0]) < 1:
        return m

    tR = 0
    tC = 0
    dR = len(m) - 1
    dC = len(m[0]) - 1

    while tR < dR:
        rotate_edge(m, tR, tC, dR, dC)
        tR += 1
        tC += 1
        dR -= 1
        dC -= 1

    print_matrix(m)


def rotate_edge(m, tR, tC, dR, dC):
    times = dC - tC
    tmp = 0
    # 边界的四点交换
    for i in range(times):
        tmp = m[tR][tC + i]
        m[tR][tC + i] = m[dR - i][tC]
        m[dR - i][tC] = m[dR][dC - i]
        m[dR][dC - i] = m[tR + i][dC]
        m[tR + i][dC] = tmp


def print_matrix(m):
    for i in range(len(m)):
        print(str(m[i]))


if __name__ == '__main__':
    m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    rotate_matrix(m)


