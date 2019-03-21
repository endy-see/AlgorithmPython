"""
设计RandomPool结构
题目：设计一种结构，在该结构中有如下三个功能：
insert(key):将某个key加入到该结构，做到不重复加入
delete(key):将原本在结构中的某个key移除
getRandom():等概率随机返回结构中的任何一个key
要求：Insert、delete和getRandom方法的时间复杂度都是O(1)
"""

import random


class Pool:
    def __init__(self):
        self.key_index_dict = dict()
        self.index_key_dict = dict()
        self.size = 0

    def insert(self, key):
        if key not in self.key_index_dict:
            self.key_index_dict[key] = self.size
            self.index_key_dict[self.size] = key
            self.size += 1

    def delete(self, key):
        if key in self.key_index_dict:
            delete_index = self.key_index_dict.get(key)
            last_index = self.size - 1
            self.size -= 1

            # 先用last_index、last_key把delete_index填上
            last_key = self.index_key_dict[last_index]
            self.key_index_dict[last_key] = delete_index
            self.index_key_dict[delete_index] = last_key
            # 再把key 和 last_index(index_key_dict的最后一个index)删掉
            self.key_index_dict.pop(key)
            self.index_key_dict.pop(last_index)

    def get_random(self):
        if self.size == 0:
            return None
        random_index = int(random.random() * self.size)
        return self.index_key_dict.get(random_index)


if __name__ == '__main__':
    pool = Pool()
    pool.insert('zhao')
    pool.insert('yan')
    pool.insert('mei')
    pool.insert('huo')
    pool.insert('yin')
    print(pool.get_random())
    print(pool.get_random())
    print(pool.get_random())
    print(pool.get_random())
    print(pool.get_random())
    pool.delete('yin')
    print(pool.get_random())
