"""
给定两个字符串str和match，长度分别为N和M。实现一个算法，如果字符串str中含有子串match，
则返回match在str中的开始位置，不含有则返回-1
普通解法时间复杂度是O(N*M)
KMP解法：next相当于给了你一计血量，当匹配不动的时候，next就往右滑（前提是next能滑得动）
1）首先生成match字符串的next数组，这个数组的长度与match字符串的长度一样，
   next[i]的含义是在match[i]之前的字符串match[0:i-1]中，必须以match[i-1]结尾的后缀子串（不能包含match[0])
   与必须以match[0]开头的前缀子串（不能包含match[i-1]）最大匹配长度是多少。这个长度就是next[i]的值，
   比如match='aaaab'字符串，next[4]之前的字符串是'aaaa'，它的后缀子串和前缀子串最大匹配为'aaa'
   match='abc1abc1'，next[7]之前的字符串是'abc1abc'，它的后缀子串和前缀子串最大匹配为'abc'
2) 假设已经得到了match的next数组，假设从str[i]出发时，匹配到j位置的字符时发现与match中的字符不一致，即
   str[i..j-1]与match[0..j-i-1]一样，直到str[j]!=match[j-i]，匹配停止
   因为现在已经有了match字符串的next数组，next[j-i]的值表示match[0..j-i-1]这一段字符串前缀与后缀的最长匹配
   那么下一次的匹配检查不再像普通解法那样退回到str[i+1]重新开始与match[0]的匹配过程，
   而是直接让str[j]与match[k]进行匹配检查（k指前缀的下一个位置），在str中药匹配的位置仍是j，而不进行退回；
   对于match来说，相当于向右滑动，让match[k]滑动到与str[j]同一个位置上，然后进行后续的匹配检查
3）如何得到next
   next[0]=-1
   next[1]=0
   从左到右依次求解next，所以在求解next[i]时，next[i-1]的值已经求出。假设A=match[i],B=match[i-1],
   C是match[i]对应前缀的下一个字符，如果C==B，那么next[i]=next[i-1]+1；否则，就看C之前的前缀和后缀匹配情况
ex:
str1 = "abcabcababaccc"
match = "ababa"
"""


def getIndexOf(s, m):
    if not s or not m or len(s) < 1 or len(s) < len(m):
        return -1
    si = 0
    mi = 0
    next = get_next_array(m)
    while si < len(s) and mi < len(m):
        if s[si] == m[mi]:
            si += 1
            mi += 1
        elif next[mi] == -1:
            si += 1
        else:
            mi = next[mi]
    return si - mi if mi == len(m) else -1


def get_next_array(m):
    if len(m) == 1:
        return [-1]
    next = [0] * len(m)
    next[0] = -1
    next[1] = 0
    pos = 2
    cn = 0
    while pos < len(next):
        if m[pos-1] == m[cn]:
            next[pos] = cn+1
            pos += 1
            cn += 1
        elif cn > 0:
            cn = next[cn]
        else:
            next[pos] = 0
            pos += 1
    return next


str1 = "abcabcababaccc"
match = "ababa"
print(getIndexOf(str1, match))