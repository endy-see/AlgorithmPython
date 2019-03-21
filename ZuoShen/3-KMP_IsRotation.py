"""
判断一个s1是否是s2的旋转字符串
思路：把s2扩成s2+s2,在新字符串中KMP方法找到s1的第一个字符，如果存在则是s2的旋转
"""


def isRotation(s1, s2):
    if not s1 or not s2 or len(s1) != len(s2):
        return False
    s = s2 + s2
    return get_index_of(s, s1) != -1


def get_index_of(s, m):
    if len(s) < len(m):
        return -1
    si = 0
    mi = 0
    next = get_next(m)
    while si < len(s) and mi < len(m):
        if s[si] == m[mi]:
            si += 1
            mi += 1
        elif next[mi] == -1:
            si += 1
        else:
            mi = next[mi]

    return si - mi if mi == len(m) else -1


def get_next(m):
    if len(m) == 1:
        return [-1]
    next = [0] * len(m)
    next[0] = -1
    next[1] = 0
    pos = 2
    cn = 0
    while pos < len(next):
        if m[pos - 1] == m[cn]:
            next[pos] = cn + 1
            pos += 1
            cn += 1
        elif cn > 0:
            cn = next[cn]
        else:
            next[pos] = 0
            pos += 1
    return next


if __name__ == '__main__':
    s1 = 'yunzuocheng'
    s2 = 'zuochengyun'
    print(isRotation(s1, s2))
