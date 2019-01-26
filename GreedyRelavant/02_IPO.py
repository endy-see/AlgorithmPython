"""
输入：参数1,正数数组costs 参数2,正数数组profits 参数３,正数k　参数4，正数m
costs[i]表示i号项目的花费　profits[i]表示i号项目在扣除花费之后还能挣到的钱(利润)
k表示你不能并行，只能串行的最多做k个项目　m表示你初始的资金
说明：你每做完一个项目，马上获得的收益，可以支持你去做下一个项目
输出：你最后获得的最大钱数
"""

import heapq


class MinCostNode:
    def __init__(self, c, p):
        self.cost = c
        self.profit = p

    def __lt__(self, other):
        return self.cost < other.cost


class MaxProfitNode:
    def __init__(self, c, p):
        self.cost = c
        self.profit = p

    def __lt__(self, other):
        return self.profit > other.profit


class Solution:
    def __init__(self):
        self.min_cost_heap = []
        self.max_profit_heap = []

    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        # 先将各个节点加入到小根堆中
        for i in range(len(Profits)):
            heapq.heappush(self.min_cost_heap, MinCostNode(Capital[i], Profits[i]))

        start_capital = W
        # 不断将小根堆中启动资金小于W的项目弹出　放进大根堆
        for i in range(k):
            while self.min_cost_heap and self.min_cost_heap[0].cost <= start_capital:
                min_cost_node = heapq.heappop(self.min_cost_heap)
                heapq.heappush(self.max_profit_heap, MaxProfitNode(min_cost_node.cost, min_cost_node.profit))
            if not self.max_profit_heap:
                return start_capital
            start_capital += heapq.heappop(self.max_profit_heap).profit
        return start_capital


if __name__ == '__main__':
    profits = [1, 2, 3]
    capital = [0, 1, 1]
    solution = Solution()
    print(solution.findMaximizedCapital(2, 0, profits, capital))
