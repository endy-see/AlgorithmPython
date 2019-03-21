"""
认识并查集结构
题目：并查集（Union/Find)从名字可以看出，主要涉及两种基本操作：合并和查找
出十四并查集中的元素是不想交的，经过一系列的基本操作（Union），最终合并成一个大的集合
而在某次合并之后，有一种合理的需求：某两个元素是否已经处在同一个集合中了？即Find操作
并查集是一种不相交集合的数据结构，设有一个动态集合S={s1，s2，s3，.....sn}，每个集合通过一个代表来标识，代表就是动态集合S中的某个元素。
比如，若某个元素 x 是否在集合 s1 中(Find操作)，返回集合 s1 的代表元素即可。
这样，判断两个元素是否在同一个集合中也是很方便的，只要看find(x) 和 find(y) 是否返回同一个代表即可。
为什么是动态集合S呢？因为随着Union操作，动态集合S中的子集合个数越来越少。
数据结构的基本操作决定了它的应用范围，对并查集而言，一个简单的应用就是判断无向图的连通分量个数，或者判断无向图中任何两个顶点是否连通。
"""


class UnionFindSets:
    def __init__(self):
        self.father_dict = dict()
        self.rank_dict = dict()

    def make_sets(self, nodes):
        self.father_dict.clear()
        self.rank_dict.clear()
        for node in nodes:
            self.father_dict[node] = node
            self.rank_dict[node] = 1

    def find_father(self, node):
        father = self.father_dict[node]
        if father != node:
            father = self.find_father(father)
        # 一路打平
        self.father_dict[node] = father
        return father

    def union(self, a, b):
        if not a or not b:
            return
        a_father = self.find_father(a)
        b_father = self.find_father(b)
        if a_father != b_father:
            a_frank = self.rank_dict[a_father]
            b_frank = self.rank_dict[b_father]
            if a_frank <= b_frank:
                self.father_dict[a_father] = b_father
                self.rank_dict[b_father] = a_frank+b_frank
            else:
                self.father_dict[b_father] = a_father
                self.rank_dict[a_father] = a_frank+b_frank



