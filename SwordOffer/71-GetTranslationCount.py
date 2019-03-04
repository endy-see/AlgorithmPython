"""
把数字翻译成字符串
题目：给定一个数字，我们按照如下规则把它翻译为字符串：0翻译成'a'，1翻译成'b'，。。。，
11翻译成'l'，。。。，25翻译成'z'。一个数字可能有多个翻译。例如，12258有5种不同的翻译，
分别是'bccfi'、'bwfi'、'bczi'、'mcfi'和'mzi'。请编写一个函数，用来计算一个数字有
多少种不同的翻译方法。
思路：以12258为例分析如何从数字的第一位开始一步步计算不同翻译方法的数目。
有两种不同的选择来翻译第一位数字1.第一种选择是数字1单独翻译成'b'，后面剩下数字2258；
第二种选择是1和紧挨着的2一起翻译成'm'，后面剩下数字258.
当最开始的一个或两个数字被翻译成一个字符之后，接着翻译后面剩下的数字。显然这是个递归问题
定义f(i)表示从第i位数字开始的不同翻译的数目，则f(i)=f(i+1)+g(i,i+1)*f(i+2)
当第i位和第i+1位两位数字拼接起来的数字在10~25范围时，g(i,i+1)的值为1；否则为0
这是一个无后效性问题，存在重复的情况 需要先写出递归版本，然后再改非递归
如：12258-> 1,2258 or 12, 258
而2258 -> 2,258 or 22,58
258属于重复的计算
递归时从大问题开始自上而下分析问题，然后从最小的子问题开始自下（base case）向上解决问题
动态规划：需要一个额外的数组help保存字符串由小到大的翻译数目，最后返回help[0]
"""


class GetTranslationCount:
    def __init__(self):
        self.res = []

    # 递归版
    def get_translation_count_recur(self, number):
        if number < 0:
            return []

        # 从str(number)的0位置开始递归
        self.get_translation_count(str(number), 0, '')
        return len(self.res)

    def get_translation_count(self, num_str, index, cur_str):
        # base case
        if index > len(num_str) - 1:
            self.res.append(cur_str)
            return

        # 将index字符转换
        self.get_translation_count(num_str, index + 1, cur_str + chr(int(num_str[index]) + ord('a')))
        # 将index~index+1字符转换
        if index < len(num_str) - 1 and '10' <= num_str[index:index + 2] <= '25':
            self.get_translation_count(num_str, index + 2, cur_str + chr(int(num_str[index:index + 2]) + ord('a')))

    # 动态规划版
    def get_translation_count_dymaic(self, number):
        if number < 0:
            return []

        return self.get_translation_count1(str(number))

    def get_translation_count1(self, num_str):
        str_len = len(num_str)
        help = [0]*str_len

        for i in range(str_len-1, -1, -1):
            if i < str_len-1:
                count = help[i+1]
            else:
                count = 1
            if i < str_len-1 and '10' <= num_str[i:i+2] <= '25':
                if i < str_len-2:
                    # 此时i+2位置有内容了
                    count += help[i+2]
                else:
                    # 此时只有它自己
                    count += 1
            help[i] = count
        return help[0]


obj = GetTranslationCount()
# print(obj.get_translation_count_dymaic(12258))
print(obj.get_translation_count_dymaic(12258))
