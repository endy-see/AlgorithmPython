"""
给定一个字符串str1，只能往str1的后面添加字符变成str2。
要求1:str2必须包含两个str1，两个str1可以有重合，但是不能以同一个位置开头。
要求2:str2尽量短
最终返回str2
举例:
str1 = 123，str2 = 123123时，包含两个str1，且不以相同位置开头，且str2最短。
str1 = 123123，str2 = 123123123时，包含两个str1，且不以相同位置开头，且str2最短。
str1 = 111，str2 = 1111 时，包含两个str1，且不以相同位置开头，且str2最短。
"""


def answer(s):
    if not s or len(s) == 0:
        return ""
    if len(s) == 1:
        return s + s
    if len(s) == 2:
        return s + s[0] if s[0] == s[1] else s + s

    end_next = end_next_len(s)
    return s + s[end_next:]


def end_next_len(s):
    next = [0] * (len(s) + 1)
    next[0] = -1
    next[1] = 0
    pos = 2
    cn = 0
    while pos < len(next):
        if s[pos-1] == s[cn]:
            next[pos] = cn+1
            pos += 1
            cn += 1
        elif cn > 0:
            cn = next[cn]
        else:
            next[pos] = 0
            pos += 1

    return next[-1]


if __name__ == '__main__':
    print(answer('a'))
    print(answer('aa'))
    print(answer('ab'))
    print(answer('abcdabcd'))
    print(answer('abracadabra'))
