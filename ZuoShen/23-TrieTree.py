"""
前缀树
何为前缀树？如何生成前缀树？
例子：一个字符串类型的数组arr1，另一个字符串类型的数组arr2，
1）arr2中有哪些字符，是arr1中出现的？请打印
2）arr2中有哪些字符，是作为arr1中某个字符串前缀出现的？请打印
3）arr2中出现次数最大的前缀

前缀树又称查找数或键树，是一种树形结构，也是一种哈希树的变种
典型的应用是用于统计和排序大量的字符串（但不仅限于字符串），所以经常被搜索引擎系统用于文本词频统计
优点：最大限度地减少无谓的字符串比较，查询效率比哈希表高。它有3个基本性质：
1）根节点不包含字符，除根节点外每一个节点都只包含一个字符
2）从根节点到某一节点，路径上经过的字符连接起来，为该节点对应的字符串
3）每个节点的所有子节点包含的字符都不相同
"""


class TrieNode:
    def __init__(self):
        self.path = 0
        self.end = 0
        self.map = [None] * 26


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s):
        if not s:
            return

        cur = self.root
        for i in range(len(s)):
            index = ord(s[i]) - ord('a')
            if not cur.map[index]:
                cur.map[index] = TrieNode()
            cur = cur.map[index]
            cur.path += 1
        cur.end += 1

    def delete(self, s):
        if self.search(s):
            cur = self.root
            for i in range(len(s)):
                index = ord(s[i]) - ord('a')
                if cur.map[index].path == 1:
                    cur.map[index] = None
                    return
                else:
                    cur.map[index].path -= 1
                cur = cur.map[index]
            cur.end -= 1

    def search(self, s):
        if not s:
            return False
        cur = self.root
        for i in range(len(s)):
            index = ord(s[i]) - ord('a')
            if not cur.map[index]:
                return False
            cur = cur.map[index]
        return cur.end != 0

    def prefix_num(self, pre):
        if not pre:
            return 0
        cur = self.root
        for i in range(len(pre)):
            index = ord(pre[i]) - ord('a')
            if not cur.map[index]:
                return 0
            cur = cur.map[index]
        return cur.path


if __name__ == '__main__':
    trie = Trie()
    print(trie.search('zhao'))
    trie.insert('zhao')
    print(trie.search('zhao'))
    trie.delete('zhao')
    print(trie.search('zhao'))
    trie.insert('zhao')
    trie.insert('zhao')
    trie.delete('zhao')
    print(trie.search('zhao'))
    trie.delete('zhao')
    print(trie.search('zhao'))
    trie.insert('zhaoa')
    trie.insert('zhaoac')
    trie.insert('zhaoab')
    trie.insert('zhaoad')
    trie.delete('zhaoa')
    print(trie.search('zhaoa'))
    print(trie.prefix_num('zhao'))

