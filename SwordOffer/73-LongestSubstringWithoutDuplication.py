"""
最长不含重复字符的子字符串
题目：请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长字符串的长度。
假设字符串中只包含'a'~'z'的字符。例如，在字符串'arabcacfr'中，最长的不含重复
字符的子字符串是'acfr'，长度为4
思路：
方法一：暴力法，找出字符串的所有子字符串O(n^2)，然后判断每个子字符串是否包含重复的字符O(n) 效率低O(n^3)
方法二：窗口法 如果当前窗口的字符串长度大于最大字符串长度，就更新最大字符串及其长度 其实就是动态规划
下面列出了两种实现方式
"""


def longest_substring_without_duplication(string):
    if not string or len(string) < 1:
        return 0

    max_len_str = ''
    max_len = 0
    left = 0
    right = 0
    while right < len(string):
        cur_str = ''
        while right < len(string) and string[right] not in cur_str:
            cur_str += string[right]
            right += 1

        if len(cur_str) > max_len:
            max_len_str = cur_str
            max_len = len(cur_str)
        left += 1
        right = left

    return max_len


def lengthOfLongestSubstring(string):
    start = max_length = 0
    used_char = {}

    for i in range(len(string)):
        if string[i] in used_char and start <= used_char[string[i]]:
            start = used_char[string[i]] + 1
        else:
            max_length = max(max_length, i - start + 1)

        used_char[string[i]] = i

    return max_length


print(longest_substring_without_duplication('arabcacfr'))
print(lengthOfLongestSubstring('arabcacfr'))
