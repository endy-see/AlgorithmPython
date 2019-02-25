"""
栈的压入、弹出序列
题目：输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为
该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1，2，3，4，5是某栈的压入
顺序，序列4，5，3，2，1是该栈序列对应的一个弹出序列，但4，3，5，1，2就不可能
是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
思路:
如果下一个弹出的数字刚好是栈顶数字，那么直接弹出；
如果下一个弹出的数字不在栈顶，则把压栈序列中还没有入栈的数字压入辅助栈，
直到把下一个需要弹出的数字压入栈顶为止；如果所有数字都压入栈后仍没有找到下一个
弹出的数字，那么该序列不可能是一个弹出序列
"""


# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV or not popV or len(pushV) != len(popV):
            return False

        help = []
        pop_index = 0
        for i in range(0, len(pushV)):
            # 先将pushV[i]入栈
            help.append(pushV[i])
            while help and help[-1] == popV[pop_index]:
                help.pop()
                pop_index += 1

        if not help and pop_index == len(popV):
            return True
        else:
            return False


obj = Solution()
pushV = [1, 2, 3, 4, 5]
popV = [4, 5, 3, 2, 1]
print(obj.IsPopOrder(pushV, popV))
