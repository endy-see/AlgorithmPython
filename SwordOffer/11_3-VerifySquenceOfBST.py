"""
题目：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果
如果是则返回true，否则返回false。假设输入的数组的任意两个数字都互不相同。
例如，输入数组{5, 7, 6, 9, 11, 10, 8}，则返回true。
        8
    6       10
 5     7  9    11
如果输入数组{7, 4, 6, 5}，则由于没有哪颗二叉搜索树的后序遍历结果是这个序列，因此返回false

二叉搜索树：又称二叉排序树，它或者是一棵空树，或者是具有下列性质的二叉树：
若它的左子树不为空，则左子树上所有节点的值均小于它的根节点的值；
若它的右子树不为空，则右子树上所有节点的值均大于它的根节点的值；
它的左、右子树也分别为二叉搜索树

思路：
在后序遍历得到的序列中，最后一个数字是树的根节点的值。数组中前面的数字可以分为两部分：
第一部分是左子树节点的值，它们都比根节点的值小；
第二部分是右子树节点的值，它们都比根节点的值大。
注意：
1. 二分查找第一个比根节点大的值的位置在本题不适用
2. 特别注意root有左子树没有右子树的情况，因为顺序查找时找不到第一个比root大的数
   对有右子树没左子树的情况，会在is_left_bst的判断条件中进行等于0情况的处理
"""


# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence or len(sequence) < 1:
            return False
        if len(sequence) == 1:
            return True

        root = sequence[-1]
        # 找到第一个大于root的值的位置（此处只能用顺序遍历的方法）
        first_big_root_index = -1
        for value in sequence:
            if value > root:
                first_big_root_index = sequence.index(value)
                break
        # 没有右子树的情况（sequence中所有数都比root小）
        if first_big_root_index == -1:
            return self.VerifySquenceOfBST(sequence[0:len(sequence)-1])
        # 没有左子树的情况会由下面的is_left_bst的判断条件来过滤掉不合乎要求的情况
        # 如果array是二叉搜索树的后序遍历，则first_big_root_index右边的所有元素都应该大于root
        for i in range(first_big_root_index, len(sequence)):
            if sequence[i] < root:
                return False

        # 这里已经确保了first_big_root_value_index左边的值都小于root，右边的值都大于root了
        # 然后分别判断左子树是否是二叉搜索树、右子树是否是二叉搜索树
        is_left_bst = True
        if first_big_root_index > 0:
            is_left_bst = self.VerifySquenceOfBST(sequence[0:first_big_root_index])

        is_right_bst = True
        if first_big_root_index < len(sequence) - 1:
            is_right_bst = self.VerifySquenceOfBST(sequence[first_big_root_index:-1])

        return is_left_bst and is_right_bst

    # 此处不能用二分查找 因为数组中的值并非一定是二叉搜索树的后序遍历结果，中间可能出现错值，从而误导了判断
    # （pass）循环二分查找数组中第一个大于target值的位置
    def get_first_big_root_index(self, array, left, right, target):
        if right - left == 1:
            return right

        mid = (left + right) >> 2
        if array[mid] > target:
            right = mid
        elif array[mid] < target:
            left = mid
        return self.get_first_big_root_index(array, left, right, target)


obj = Solution()
# sequence=[5, 7, 6, 9, 11, 10, 8]
# sequence = [4, 6, 7, 5]
sequence = [7, 4, 6, 5]
print(obj.VerifySquenceOfBST(sequence))
