"""
折纸问题
题目：请把一段纸条竖着放在桌子上，然后从纸条的下边向上方对折1次，压出折痕后展开。
此时折痕是凹下去的，即折痕凸起的方向指向纸条的背面。如果从纸条的下边向上方连续对折2次，
压出折痕后展开，此时有三条折痕，从上到下依次是下折痕、下折痕和上折痕
给定一个输入参数N，代表纸条都从下边向上方连续对折N次，请从上到下打印所有折痕的方向。
例如：N=1时，打印：down
     N=2时，打印：down down up
     N=3时，打印：down down up down down up up
         down
    down       up
down    up  down  up
思路：二叉树的先序遍历
"""


def printAllFolds(N):
    print_process(1, N, True)


def print_process(i, N, is_down):
    if i > N:
        return
    print_process(i+1, N, True)
    if is_down:
        print('down')
    else:
        print('up')
    print_process(i+1, N, False)


if __name__ == '__main__':
    printAllFolds(2)
    # printAllFolds(3)


