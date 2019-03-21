"""
汉诺塔问题
题目：给定一个整数n，代表汉诺塔游戏中从小到大放置的n个圆盘
假设开始时所有的圆盘都放在左边的柱子上，想按照汉诺塔游戏的要求把所有的圆盘都移到右边的柱子上
实现函数打印最优移动轨迹
"""


def hanoi(n):
    if n > 0:
        process(n, 'left', 'mid', 'right')


def process(n, From, Mid, To):
    if n == 1:
        print('move from ' + From + ' to ' + To)
    else:
        process(n - 1, From, To, Mid)
        process(1, From, Mid, To)
        process(n - 1, Mid, From, To)


hanoi(3)


