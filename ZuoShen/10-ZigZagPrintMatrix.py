"""
"之"字形打印
题目：给定一个矩阵matrix，按照"之"字形的方式打印这个矩阵，例如
1, 2, 3, 4,
5, 6, 7, 8,
9, 10, 11, 12
"之"字形打印的结果为：1,2,5,9,6,3,4,7,10,11,8,12
要求：额外空间复杂度O(1)
"""


def zigzag_print(m):
    if not m or len(m) < 1 or not m[0] or len(m[0]) < 1:
        return m

    tR = 0
    tC = 0
    dR = 0
    dC = 0
    endR = len(m) - 1
    endC = len(m[0]) - 1
    # 第一行默认从下向上（行减列加）；如果是从上往下打，则行加列减
    from_up = False
    while tR != endR + 1:
        print_level(m, tR, tC, dR, dC, from_up)
        tR = tR + 1 if tC == endC else tR
        tC = tC if tC == endC else tC + 1
        dC = dC + 1 if dR == endR else dC
        dR = dR if dR == endR else dR + 1
        from_up = not from_up


def print_level(m, tR, tC, dR, dC, from_up):
    if from_up:
        while tR != dR + 1:
            print(m[tR][tC])
            tR += 1
            tC -= 1
    else:
        while dR != tR - 1:
            print(m[dR][dC])
            dR -= 1
            dC += 1


if __name__ == '__main__':
    m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    zigzag_print(m)


