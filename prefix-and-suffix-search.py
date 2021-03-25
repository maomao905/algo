"""
Trie

1. traverse trie from the head
2. going back from the end and check it matches suffix and leave pass the largest index back
"""
from typing import List
class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = {}
        for i, word in enumerate(words):
            node = self.trie
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['*'] = i

    def f(self, prefix: str, suffix: str) -> int:
        N=len(prefix)
        def dfs(node, i):
            if i < N:
                c = prefix[i]
                if c not in node:
                    return -1
                node = node[c]
                return dfs(node, i+1)
            else:
                if 
                for _c in node:
                    dfs(node[_c], i)
        
        return dfs(self.trie, 0)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
