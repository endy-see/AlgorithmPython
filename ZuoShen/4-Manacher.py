"""
Manacher算法：
给定一个字符串s，返回s中最长回文子串的长度
例如：s='123'，其中的最长回文子串为'1'、'2'或'3'，所以返回1
s='abc1234321ab'，其中最长的回文子串为'1234321'，所以返回7
思路：
1. 先说一个很好理解的方法：奇回文 偶回文
   从左到右遍历字符串，遍历到每个字符的时候，都看看以这个字符作为中心能够产生多大的回文字符串
   这种方法只要解决奇回文和偶回文寻找方式的不同就可以了
   此方法的缺点：之前遍历过的字符完全无法指导后面遍历的过程，即对每个字符来说都是从自己的位置出发，往左右两个方向扩出去检查
   这样，对每个字符来说，往外扩的代价都是一个级别的O(N)，所以总体时间复杂度O(N^2)
2. Manachar算法可以做到O(N)，精髓是之前字符的"扩"过程，可以指导后面字符的"扩"过程，使得每次的"扩"过程都不是从无开始
   步骤：
   1）对s处理：把每个字符开头、结尾和中间插入一个特殊字符'#'
   2）优化'扩'过程： 3个辅助变量
      pArr：p_arr[i]表示以s[i]作为回文中心的情况下，扩出去得到的最大回文半径是多少
      pR：表示之前遍历的所有字符的所有回文半径，最右即将到达的位置
      index：表示最近一次pR更新时，那个回文中心的位置
   3）分两种情况：
   -1：i在pR外（即pR未能包含住i）：暴力扩 O(N)
   -2：i在pR内又可以分3中情况（i'表示i关于index的对称位置，即i'=2*index-i）：
     2-1：i'在L、R内     O(1)  i位置的最大回文右边界就是i'对应的最大回文右边界：pArr[2*index-i]
     2-2：i'在L、R外     O(1)  最大回文右边界就是距离边界的大小：pR-i
     2-3：i'在L上（压线） O(N)  最大回文右边界不需要验证的部分是pR-i，但是再往右的话还是需要验证的（即代码中的while部分）
"""
import sys


# '扩'
def manacher_str(s):
    res = [None] * (len(s) * 2 + 1)
    index = 0
    for i in range(len(res)):
        if i & 1 == 0:
            res[i] = '#'
        else:
            res[i] = s[index]
            index += 1

    return res


# 返回s中最大回文串的长度
def max_lcps_len(s):
    if not s or len(s) < 1:
        return 0

    s = manacher_str(s)
    pArr = [0] * len(s)
    index = -1
    pR = -1
    max_len = -sys.maxsize
    for i in range(len(s)):
        if pR > i:
            # 情况二：最大回文右边界包含了当前的i位置，那么i位置的回文右边界可以直接取
            # pR-i和pArr[2*index-i]（i位置关于index对称的位置i'）中较小的一个
            # 即如果pArr[2*index-i]=i'的最大回文长度如果超出了左边界（对称到右边就是超出了pR-i)，则pArr[i]取pR-i
            pArr[i] == min(pArr[2*index-i], pR-i)
        else:
            # pR-1位置没有包住当前的i位置->暴力扩（和普通做法一样，从i位置字符开始，向左右两侧扩出去检查，此时扩的过程没有加速）
            pArr[i] = 1

        while i+pArr[i] < len(s) and i - pArr[i] > -1:
            # 当扩的位置没有超过边界时，只要关于i左右相等，就持续扩
            if s[i+pArr[i]] == s[i-pArr[i]]:
                pArr[i] += 1
            else:
                break

        if i + pArr[i] > pR:
            # 以i为中心的回文串向右能扩到超过pR的位置，则更新最大回文右边界及其对称中心
            pR = i + pArr[i]
            index = i
        max_len = max(max_len, pArr[i])
    return max_len - 1


if __name__ == '__main__':
    # print(manacher_str('abc'))
    print(max_lcps_len('abc1234321ab'))
