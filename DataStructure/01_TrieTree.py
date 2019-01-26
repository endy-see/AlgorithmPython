"""
前缀树
何为前缀树？　有一个根节点　该根节点下面连接了不同的字符路径
如何生成前缀树？　字母是写在路径上而不是节点上的
例子：
一个字符串类型的数组arr1,另一个字符串类型的数组arr2
1. arr2中有哪些字符，是arr1中出现的？请打印 search()
2. arr2中有哪些字符，是作为arr1中某个字符串前缀出现的？请打印  prefix_number
3. arr2中出现次数最大的前缀
"""


class TrieNode:
    def __init__(self):
        # 有多少字符串经过当前路径
        self.path = 0
        # 有多少字符串是以当前路径结尾的
        self.end = 0
        # 后面连接了哪些路径（长度为26的列表）
        self.nexts = [None] * 26


class TrieTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        '''Add a string to this trie'''
        if word is None:
            return
        str_len = len(word)
        node = self.root
        for i in range(str_len):
            # ord[str[i]]:求字符str[i]的ascii码
            index = ord(word[i]) - ord('a')
            if node.nexts[index] is None:
                node.nexts[index] = TrieNode()
            node = node.nexts[index]
            # 先让根节点窜下来　然后当前节点的结果路径才加１
            node.path = node.path + 1
        # node不断往下窜　窜到最后一个节点时end才加１
        node.end = node.end + 1

    def search(self, word):
        '''search if this word in trie'''
        if word is None:
            return 0
        str_len = len(word)
        node = self.root
        for i in range(str_len):
            index = ord(word[i]) - ord('a')
            if node.nexts[index] is None:
                return 0
            node = node.nexts[index]
        return node.end

    def delete(self, word):
        '''delete a string from this trie'''
        if self.search(word) != 0:
            str_len = len(word)
            node = self.root
            for i in range(str_len):
                index = ord(word[i]) - ord('a')
                if node.nexts[index].path - 1 == 0:
                    node.nexts[index] = None
                    return
                node.nexts[index].path = node.nexts[index].path - 1
                node = node.nexts[index]
            node.end = node.end - 1

    def prefix_number(self, pre):
        '''前缀树中有多少个字符串是以pre作为前缀的'''
        if pre is None:
            return 0
        str_len = len(pre)
        node = self.root
        for i in range(str_len):
            index = ord(pre[i]) - ord('a')
            if node.nexts[index] is None:
                return 0
            node = node.nexts[index]
        return node.path


if __name__ == '__main__':
    trie = TrieTree()
    print(trie.search('zuo'))
    trie.insert('zuo')
    print(trie.search('zuo'))
    trie.delete('zuo')
    print(trie.search('zuo'))
    trie.insert('zuo')
    trie.insert('zuo')
    trie.insert('zuo')
    print(trie.search('zuo'))
    trie.delete('zuo')
    print(trie.search('zuo'))
    trie.insert('zuoa')
    trie.insert('zuoac')
    trie.insert('zuoab')
    trie.insert('zuoad')
    trie.insert('zuoa')
    print(trie.search('zuo'))
    print(trie.prefix_number('zuo'))




