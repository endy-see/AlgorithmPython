"""
数组中唯一只出现一次的数字
题目：在一个数组中除一个数字只出现一次之外，其他数字都出现了三次。
请找出那个只出现一次的数字
ex: [3, 5, 5, 5, 8, 8, 8]
思路：这里不能用异或的思路，但是可以用位运算的思路
如果一个数字出现三次，那么它的二进制表示的每一位（0或者1）也出现3次。
如果把所有出现三次的数字的二进制表示的每一位都分别加起来，那么每一位、
的和都能被3整除。反之，若某一位的和不能被3整除，那么只出现一次的数字
二进制表示中对应的某一位是1
时间复杂度O(n) 空间复杂度O(1)
此题还有另外另种解法，但是都没这种解法好：
1. 排序，从排序的数组中找到只出现一次的数字 时间复杂度O(nlogn)
2. 哈希表，用一个哈希表来记录数组中每个数字出现的次数，额外空间复杂度O(n)
"""


def FindNumberAppearingOnce(arr):
    if not arr or len(arr) < 1:
        return arr
    # 创建一个32维数组 用来存放所有数字的所有位中1的个数
    help = [0] * 32
    for i in range(0, len(arr)):
        set_1_nums(help, arr[i])

    res = 0
    for i in range(0, len(help)):
        help[i] %= 3
        if help[i] != 0:
            res += 1 << i

    return res


# 若num的某一位为1，则help对应位自加1
def set_1_nums(help, num):
    move_1 = 1
    for i in range(0, 32):
        if move_1 & num != 0:
            help[i] += 1
        move_1 <<= 1


arr =  [6, 6, 6, 1, 5, 5, 5, 8, 8, 8]
print(FindNumberAppearingOnce(arr))