"""
(TLE)
- preprocess all possible chars
build 26*100*100*100
search 100

- use *
100 * 100 words * 100 length
100 calls * 100 words * 100 length
"""
from typing import List
class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def buildDict(self, dictionary: List[str]) -> None:
        for w in dictionary:
            cur = self.trie
            for i in range(len(w)):
                cur = self.trie if i == 0 else cur[w[i-1]]
                for j in range(26):
                    char = chr(ord('a') + j)
                    _w = char + w[i+1:]
                    # skip exactly same word
                    if w[i] == char:
                        if char not in cur:
                            cur[char] = {}
                        continue
                    
                    node = cur
                    for c in _w:
                        if c not in node:
                            node[c] = {}
                        node = node[c]
                    node['*'] = True

    def search(self, searchWord: str) -> bool:
        node = self.trie
        for c in searchWord:
            if c not in node:
                return False
            node = node[c]
        return '*' in node

"""
trie

try different chars in search
- build trie len(dict) * len(word) O(100^2)
- search 26 * len(searchword) O(26*100 length*100calls)
"""

class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def buildDict(self, dictionary: List[str]) -> None:
        for w in dictionary:
            node = self.trie
            for c in w:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['*'] = {}

    def search(self, w: str) -> bool:
        N=len(w)
        def dfs(node, i, used):
            if i == N:
                return used and '*' in node
            
            if used:
                if w[i] not in node:
                    return False
                return dfs(node[w[i]], i+1, used)
            else:
                # skip
                if w[i] in node and dfs(node[w[i]], i+1, used):
                    return True
                
                # use
                for j in range(26):
                    c = chr(ord('a') + j)
                    if c == w[i]:
                        continue
                    if c in node and dfs(node[c], i+1, True):
                        return True
                return False
        return dfs(self.trie, 0, False)
                    


d = MagicDictionary()
d.buildDict(['hello', 'hallo', 'leetcode'])
print(d.search('hello'))
print(d.search('hallo'))
print(d.search('hell'))
print(d.search('leedaode'))
