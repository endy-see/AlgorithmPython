"""
做项目获最大收益
输入：
参数1：正数数组costs       cost[i]表示i号项目的花费
参数2：正数数组profits     profits[i]表示i号项目在扣除花费之后还能挣到的钱（利润）
参数3：正数k              k表示你不能并行、只能串行的最多做k个项目
参数4：正数m              m表示你初始的资金
说明：你每做完一个项目，马上获得的收益，可以支持你去做下一个项目
输出：你最后获得的最大钱数

思路：贪心思想和堆结构
两个堆，代价低的项目组成小根堆，按收益最大组成大根堆
时间复杂度：O(N*logN)
解决：
1.创建一个类，实现优先级队列功能
2.使用优先级队列求解IPO问题
"""


class PriorityQueue:
    def __init__(self, comparator=lambda x, y: x > y):
        self._lst = []
        self.comparator = comparator

    def __heap_insert(self, index):
        array = self._lst
        while index != 0 and self.comparator(array[index], array[(index - 1) >> 1]):
            array[index], array[(index - 1) >> 1] = array[(index - 1) >> 1], array[index]
            index = (index - 1) >> 1

    def __heap_ify(self, index, size):
        array = self._lst
        left = 2 * index + 1
        while left < size:
            # 选出左右孩子中的最值
            largest = left
            right = left + 1
            if right < size:
                largest = left if self.comparator(array[left], array[right]) else right

            if self.comparator(array[index], array[largest]):
                break

            array[index], array[largest] = array[largest], array[index]
            index = largest
            left = 2 * index + 1

    def is_empty(self):
        return True if len(self._lst) == 0 else False

    def add(self, obj):
        self._lst.append(obj)
        self.__heap_insert(len(self._lst) - 1)

    def pop(self):
        self._lst[0], self._lst[-1] = self._lst[-1], self._lst[0]
        obj = self._lst.pop()
        self.__heap_ify(0, len(self._lst))
        return obj

    def peek(self):
        return self._lst[0]

    poll = pop


class Project:
    def __init__(self, c, p):
        self.cost = c
        self.profit = p


def max_heap_comparator(obj1, obj2):
    return obj1.profit > obj2.profit  # 大根堆


def min_heap_comparator(obj1, obj2):
    return obj1.cost < obj2.cost  # 小根堆


def findMaximizedCapital(costs: list, profits: list, k: int, m: int) -> int:
    min_cost_heap = PriorityQueue(min_heap_comparator)
    max_profit_heap = PriorityQueue(max_heap_comparator)

    for cost, profit in zip(costs, profits):
        min_cost_heap.add(Project(cost, profit))

    for i in range(0, k):
        while not min_cost_heap.is_empty() and min_cost_heap.peek().cost <= m:
            obj = min_cost_heap.pop()
            max_profit_heap.add(obj)

        if max_profit_heap.is_empty():
            break
        m += max_profit_heap.poll().profit
    return m


if __name__ == '__main__':
    costs = [2, 10, 14, 1]
    profits = [5, 20, 8, 10]
    k = 4
    m = 15
    ret = 0
    ret = findMaximizedCapital(costs, profits, k, m)
    print(ret)
