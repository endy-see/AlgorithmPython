"""
剪绳子
题目：给你一根长度为n的绳子，请把绳子剪成m段（m、n都是整数，n>1且m>1），
每段绳子的长度记为k[0], k[1],...,k[m]。请问k[0]*k[1]*...*k[m]可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18

思想：动态规划
动态规划的特点：
1. 求一个问题的最优解
2. 整体问题的最优解是依赖各个子问题的最优解
3. 把大问题分解成若干个小问题，这些小问题之间还有相互重叠的更小的子问题
4. 从上往下分析问题，从下往上解决问题
由于子问题在分解大问题的过程中重复出现，为了避免重复求解子问题，我们可以
用从下往上的顺序，先计算小问题的最优解并存储下来，再以此为基础求取大问题的最优解
贪婪算法和动态规划的区别：
当我们用贪婪算法解决问题的时候，每一步都可以做出一个贪婪的选择，基于这个选择，
我们确定能够得到最优解。至于为什么这样的贪婪选择能得到最优解，是需要数学方式证明的
下面证明贪婪算法的正确性。
1）首先，当n>=5时，可以证明2(n-2)>n, 3(n-3)>n。即当绳子剩下的长度大于或者等于5的时候，
   我们就把它剪成长度为3或者2的绳子段。
2) 另外，当n>=5时，3(n-3)>2(n-2)，所以应该尽可能地多剪长度为3的绳子段
3）上面证明的前提是n>=5，但是当绳子的长度为4的时候，2*2>1*3，
所以当绳子长度为4时其实没有必要剪，只是题目要求至少剪一刀
"""


# 法一：动态规划
# 传入参数为绳长
def maxProductAfterCutting(rope_length):
    # 由底向上
    if rope_length < 2:
        return 0
    if rope_length == 2:
        return 1
    if rope_length == 3:
        return 2

    # 申请额外数组，用于存放子问题的最优解
    # 数组中第i个元素表示把长度为i的绳子剪成若干段之后各段长度乘积的最大值，即f(i)
    products = [0] * (rope_length + 1)
    products[0] = 0
    products[1] = 1
    products[2] = 2
    products[3] = 3

    max_product = 0
    for i in range(4, rope_length + 1):
        for j in range(1, i // 2 + 1):
            product = products[j] * products[i - j]
            if product > max_product:
                max_product = product
        products[i] = max_product
        max_product = 0
    return products[-1]


# 法二：贪婪算法
# 如果我们按照如下的策略来剪绳子，则得到的各段绳子的长度的乘积将最大：
# 当n>=5时，我们尽可能多地剪长度为3的绳子；
# 当剩下的绳子长度为4时，把绳子剪成两段长度为2的绳子
def maxProductAfterCutting1(rope_length):
    if rope_length < 2:
        return 0
    if rope_length == 2:
        return 1
    if rope_length == 3:
        return 2
    if rope_length == 4:
        return 4

    # 尽可能多地剪去长度为3的绳子段
    three_num = rope_length // 3

    # 当绳子最后剩下的长度为4的时候，不能再剪去长度为3的绳子段，因为2*2>1*3
    if rope_length - three_num*3 == 1:
        three_num -= 1

    two_num = (rope_length - three_num * 3) // 2
    return pow(3, three_num)*pow(2, two_num)


# test
print(maxProductAfterCutting1(4))
print(maxProductAfterCutting1(5))
print(maxProductAfterCutting1(6))
print(maxProductAfterCutting1(7))
# print(maxProductAfterCutting1(8))
