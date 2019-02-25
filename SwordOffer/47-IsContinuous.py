"""
扑克牌中的顺子
题目：从扑克牌中随机抽取5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
2~10为数字本身，A为1， J为11， Q为12， K为13，而大小王可以看成任意数字
为了方便起见，你可以认为大小王是0
ex：[A, 3, 0, 0, 5] 则认为是顺子
思路：
1. 首先把数组排序
2. 其次统计数组中0的个数
3. 最后统计排序之后的数组中相邻数字之间的空缺总数。如果空缺的总数小于或者等于0
的个数，那么这个数组就是连续的；反之则不连续
注意：如果数组中的非0数字重复出现，则该数组不是连续的（如果一副牌里有对子就不是顺子）
"""


# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers or len(numbers) < 1:
            return False
        res = sorted(numbers)
        # 统计0的个数
        num0 = 0
        gap = 0
        gap_first = -1
        is_shunzi_start = False
        for i in range(len(res)):
            if res[i] == 0:
                num0 += 1
            else:
                is_shunzi_start = True

            if is_shunzi_start:
                if gap_first == -1:
                    gap_first = res[i]
                else:
                    if res[i] == gap_first:
                        return False
                    gap += res[i] - gap_first - 1
                    gap_first = res[i]

        return gap <= num0


obj = Solution()
arr = [1, 3, 2, 6, 4]
arr = [1, 3, 2, 5, 4]
print(obj.IsContinuous(arr))