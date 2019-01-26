"""
并查集: 合并和查找
相关题目：将多个集合合并成没有交集的集合
给定一个字符串的集合，格式如：{aaa, bbb, ccc}, {bbb, ddd}, {eee, fff}, {ggg}, {ddd, hhh}
要求将其中交集不为空的集合合并，要求合并完成的集合之间无交集　，例如上例应输出：
{aaa, bbb, ccc, ddd, hhh}, {eee, fff}, {ggg}
(1)请描述你解决这个问题的思路
(2)给出主要的处理流程，算法，以及算法的复杂度
(3)请描述可能的改进
"""


class Node:
    def __init__(self, data):
        self.value = data


class UnionFindSet:
    def __init__(self, node_list):
        self.father_dict = {}
        self.size_dict = {}
        for node in node_list:
            self.father_dict[node] = node
            self.size_dict[node] = 1

    def find_head(self, node):
        # 找到节点node所在集合的代表节点 找头节点的过程中就不断地将当前及以上节点打乱顺序
        father = self.father_dict[node]
        if father != node:
            father = self.find_head(father)
        self.father_dict[node] = father
        return father

    def is_same_set(self, node_a, node_b):
        # 查询两个节点是否属于同一个集合　即查看这两个节点的代表节点是否是同一个
        head_a = self.find_head(node_a)
        head_b = self.find_head(node_b)
        return head_a == head_b

    def union(self, node_a, node_b):
        if node_a is None or node_b is None:
            return
        # 把size小的集合并到size大的集合中
        head_a = self.find_head(node_a)
        head_b = self.find_head(node_b)
        if head_a != head_b:
            size_a = self.size_dict[node_a]
            size_b = self.size_dict[node_b]
            if size_a < size_b:
                # 把a并到b中
                self.father_dict[head_a] = head_b
                self.size_dict[head_b] = size_a + size_b
            else:
                self.father_dict[head_b] = head_a
                self.size_dict[head_a] = size_a + size_b


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    node_list = []
    for value in a:
        node_list.append(Node(value))
    union_find_set = UnionFindSet(node_list)
    union_find_set.union(node_list[0], node_list[1])
    union_find_set.union(node_list[2], node_list[4])
    union_find_set.union(node_list[2], node_list[0])
    print(union_find_set.is_same_set(node_list[1], node_list[4]))

