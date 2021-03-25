"""
(WA)
"""
from collections import defaultdict
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.index = []
        self.i = 0
        self.len = {}
        self.len_exists = {}

    def addWord(self, word: str) -> None:
        N=len(word)
        for i in range(N):
            if len(self.index) == i:
                d = defaultdict(set)
                self.index.append(d)
            self.index[i][word[i]].add(self.i)
        self.len[self.i] = len(word)
        self.len_exists[len(word)] = True
        self.i += 1

    def search(self, word: str) -> bool:
        N=len(word)
        if N > len(self.index):
            return False
        
        ids = set()
        for i in range(N):
            if word[i] == '.':
                continue
            
            if not ids:
                ids = self.index[i][word[i]]
            else:
                ids &= self.index[i][word[i]]
            
            if len(ids) == 0:
                return False
        
        if ids:
            return any(self.len[id] == N for id in ids)
        else:
            return N in self.len_exists
                
"""
Trie

but O(26^N) where N is the search word length is impractical
"""

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        node = self.trie
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['*'] = {}
        

    def search(self, word: str) -> bool:
        N=len(word)
        def dfs(i, node):
            if i == N:
                return '*' in node
            
            c = word[i]
            i += 1
            if c == '.':
                return any(dfs(i, node[_c]) for _c in node)
            elif c in node:
                return dfs(i, node[c])
            
            return False
        
        return dfs(0, self.trie)
            
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


# Your WordDictionary object will be instantiated and called as such:
d = WordDictionary()
d.addWord('bad')
d.addWord('dad')
d.addWord('mad')
d.addWord('a')
d.addWord('ab')
print(d.search('pad'))
print(d.search('bad'))
print(d.search('.ad'))
print(d.search('b..'))
print(d.search('a.'))
print(d.search('..'))
print(d.search('b'))
