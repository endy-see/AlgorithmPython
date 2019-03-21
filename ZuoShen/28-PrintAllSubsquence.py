"""
打印给定字符串的所有子序列
"""


def printAllSubsquences(s):
    if not s or len(s) < 1:
        return
    chs = list(s)
    process(chs, 0)


def process(chs, i):
    if i == len(chs):
        print(''.join(chs))
        return
    process(chs, i + 1)
    tmp = chs[i]
    chs[i] = ''
    process(chs, i+1)
    chs[i] = tmp


printAllSubsquences('abc')

