"""
Manacher算法扩展题目
给定一个字符串str1，只能往str1的后面添加字符变成str2，要求str2整体都是回文串且最短
举例：str1=ABC12321，返回ABC12321CBA
"""


def shortest_end(src_str):
    if not src_str or len(src_str) < 1:
        return None
    s = manacher_str(src_str)
    pArr = [0] * len(s)
    index = -1
    pR = -1
    max_contains_end = -1
    for i in range(len(s)):
        pArr[i] = min(pArr[2*index-i], pR-i) if i < pR else 1
        while i+pArr[i] < len(s) and i-pArr[i] > -1:
            if s[i+pArr[i]] == s[i-pArr[i]]:
                pArr[i] += 1
            else:
                break
        if i + pArr[i] > pR:
            pR = i + pArr[i]
            index = i
        if pR == len(s):
            max_contains_end = pArr[i]
            break
    res = [None]*(len(src_str)-(max_contains_end-1))
    for i in range(len(res)):
        res[len(res)-1-i] = s[i*2+1]
    return ''.join(res)


def manacher_str(s):
    res = [None] * (len(s)*2 + 1)
    index = 0
    for i in range(len(res)):
        if i & 1 == 0:
            res[i] = '#'
        else:
            res[i] = s[index]
            index += 1

    return res


if __name__ == '__main__':
    print(shortest_end('abcd123321'))