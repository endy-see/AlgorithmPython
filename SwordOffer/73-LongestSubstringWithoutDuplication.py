"""
最长不含重复字符的子字符串
题目：请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长字符串的长度。
假设字符串中只包含'a'~'z'的字符。例如，在字符串'arabcacfr'中，最长的不含重复
字符的子字符串是'acfr'，长度为4
思路：
方法一：不好 暴力法，找出字符串的所有子字符串O(n^2)，然后判断每个子字符串是否包含重复的字符O(n) 效率低O(n^3)
方法二：不好 窗口法 如果当前窗口的字符串长度大于最大字符串长度，就更新最大字符串及其长度 其实就是动态规划
方法三：推荐做法
    1）用额外的存储空间dict，key表示某个字符，value表示该字符最近一次出现的位置
    2）然后定义两个变量
       pre：表示在必须以str[i-1]字符结尾的情况下，最长无重复子串开始位置的前一个位置，初始值为-1
       len：记录以每一个字符结尾的情况下，最长无重复字符子串长度的最大值，初始值，len=0
       然后从左到右依次遍历str，假设现在遍历到str[i]，接下来求在必须以str[i]结尾的情况下，最长无重复字符子串的长度
    3）A=map(str[i])：表示在之前的遍历中，str[i]最近出现的位置，必须以str[i]结尾的字符串：str[A+1:i]
       B=pre+1：表示必须以str[i-1]字符结尾的情况的情况下，最长无重复字符子串的开始位置：str[B:i-1]
       比较A和B哪个更靠右，哪个就是以str[i]结尾的最长无重复子串的左边界，并将这个值更新为新的pre
"""


# 低效的方式 时间复杂度O(n^2)
def longest_substring_without_duplication(s):
    if not s or len(s) < 1:
        return 0

    max_len_str = ''
    max_len = 0
    left = 0
    right = 0
    while right < len(s):
        cur_str = ''
        while right < len(s) and s[right] not in cur_str:
            cur_str += s[right]
            right += 1

        if len(cur_str) > max_len:
            max_len_str = cur_str
            max_len = len(cur_str)
        left += 1
        right = left

    return max_len


# 推荐O(n)的解法 额外空间复杂度O(m)
# n表示字符串的长度，m表示字符串中字符种类的个数
def lengthOfLongestSubstring(s):
    if not s or len(s) < 1:
        return 0

    char_recent_index_dict = {}
    pre = -1
    max_len = 0
    for i in range(len(s)):
        if s[i] in char_recent_index_dict:
            pre = max(pre, char_recent_index_dict[s[i]])
        cur = i - pre
        max_len = max(max_len, cur)
        char_recent_index_dict[s[i]] = i

    return max_len


print(longest_substring_without_duplication('arabcacfr'))
print(lengthOfLongestSubstring('arabcacfr'))
