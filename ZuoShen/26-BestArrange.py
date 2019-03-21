"""
一些项目要占用一个会议室宣讲，会议室不能同时容纳两个项目的宣讲。
给你每一个项目开始的时间和结束的时间(给你一个数组，里面是一个个具体的项目)，你来安排宣讲的日程
要求会议室进行的宣讲的场次最多。返回这个最多的宣讲场次。
思路：这个也是一个贪心算法，优先考虑的是宣讲会结束时间早的那个。
"""
import heapq

class Program:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def bestArrange(programs, start):
