'''
切金条
一块金条切成两半，是需要花费和长度值一样的铜板的
比如，长度为２０的金条，不管切成长度多大的两半，都要花费２０个铜板
一群人想整分整块金条，怎么分最省铜板？
例如：给定数组{10,20,30}，代表一共三个人，整块金条长度为10+20+30=60
金条要分成10,20,30三个部分．如果先把长度60的金条分成10和50,花费60
再把长度50的金条分成20和30，花费50，一共花费110铜板
但是如果先把长度60的金条分成30和30，花费60 再把长度30金条分成10和20，花费30
一共花费90铜板
输入一个数组，返回分割的最小代价

思想：哈夫曼编码
将数组中的数加入小根堆　每次从小根堆中取出２个数相加求和，并再将和放进堆里
直到堆为空为止
'''

import heapq


def cur_gold_bar(arr):
    arr_list = []
    for data in arr:
        heapq.heappush(arr_list, data)

    sum = 0
    while len(arr_list) > 1:
        small1 = heapq.heappop(arr_list)
        small2 = heapq.heappop(arr_list)
        cur = small1 + small2
        sum += cur
        heapq.heappush(arr_list, cur)
    return sum


if __name__ == '__main__':
    res = cur_gold_bar([10, 20, 30])
    print(res)
