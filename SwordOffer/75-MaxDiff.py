"""
股票的最大利润
题目：假设把某股票的价格按照实际先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？
例如，一只股票在某些实际节点的价格为{9,11,8,5,7,12,16,14}，如果我们在价格5买入并在价格为16时
卖出，则能收获最大的利润11。（只能在买入某只股票后才能卖出）
思路：如果把股票的买入价和卖出价两个数字组成一个数对，利润就是这个数对的差值
方法一：暴力法O(n^2)
方法二：反过来思考：定义diff(i)表示卖出价数组中第i个数字时可能获得的最大利润。
在卖出价一定时，买入价越低，获得的利润越大。即如果在扫描到数组中的第i个数字时，
只要记住前面i-1个数字中的最小值，就能算出在当前价位卖出时可能得到的最大利润
"""


# 股票的最大利润（一次卖出）
def maxProfit(prices):
    if not prices or len(prices) < 2:
        return 0

    min_price = prices[0]
    max_diff = prices[1] - min_price
    for i in range(2, len(prices)):
        if prices[i - 1] < min_price:
            min_price = prices[i - 1]
        if prices[i] - min_price > max_diff:
            max_diff = prices[i] - min_price
    return max_diff


# 股票的最大利润（多次卖出-leetcode）
# 前一天买入，盈利则第二天卖出
# 可以对股票进行多次的买入和卖出；
# 则如果第二天的价格高于第一天的价格就可以以第二天的价格卖出，卖出后立即再次买入；
# 如果第二天的价格低于第一天的价格，那么就在第一天结束前就卖出，相当于不盈利。
# 所以通过逐个相邻两数进行比较即可，如果后面的大，则记为利润
def maxProfit1(prices):
    if not prices or len(prices) < 2:
        return 0
    max_profit = 0
    for i in range(len(prices)-1):
        profit = prices[i+1] - prices[i]
        if profit > 0:
            max_profit += profit

    return max_profit
