from heapq import *
from typing import List
"""
Trie
1. traverse trie
    find the end mark and store the matching sentences
2. sort by frequency and ASCII-code order
3. return top3

if input is '#':
    add the current sentence and frequency

initialize trie O(NL)
input O(26^N) in worst
"""
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = {}
        for sentence, time in zip(sentences, times):
            node = self.trie
            for c in sentence:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['#'] = [time, sentence]
        self.cur_node = self.trie
        self.chars = []
            
    def __reset(self):
        self.cur_node = self.trie
        self.chars = []

    def input(self, c: str) -> List[str]:
        if c == '#':
            if '#' in self.cur_node:
                self.cur_node['#'][0] += 1
            else:
                self.cur_node['#'] = [1, ''.join(self.chars)]
            self.__reset()
            return []
        
        self.chars.append(c)
        if c not in self.cur_node:
            self.cur_node[c] = {}
            self.cur_node = self.cur_node[c]
            return []
        
        self.cur_node = self.cur_node[c]
        res = []
        def dfs(node):
            for c in node:
                if c == '#':
                    res.append(node['#'])
                    continue

                dfs(node[c])
                
        dfs(self.cur_node)
        items = nsmallest(3, res, lambda x: (-x[0], x[1]))
        return list(map(lambda x: x[1], items))
        


# Your AutocompleteSystem object will be instantiated and called as such:
# ["AutocompleteSystem","input","input","input","input","input","input","input","input","input","input","input","input","input","input"]
# [[["abc","abbc","a"],[3,3,3]],["b"],["c"],["#"],["b"],["c"],["#"],["a"],["b"],["c"],["#"],["a"],["b"],["c"],["#"]]
ac = AutocompleteSystem(["abc","abbc","a"],[3,3,3])
print(ac.input('a'))
# print(ac.input('c'))
# print(ac.input('#'))
# print(ac.input('b'))
# print(ac.input('c'))
# print(ac.input('#'))
# print(ac.input('a'))
# print(ac.input('b'))
# print(ac.input('c'))
# print(ac.input('#'))
# print(ac.input('a'))
# print(ac.input('b'))
# print(ac.input('c'))
# print(ac.input('#'))
# ac = AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])
# print(ac.input('i'))
# print(ac.input(' '))
# print(ac.input('a'))
# print(ac.input('#'))
# print(ac.input('i'))
# print(ac.input(' '))
# print(ac.input('a'))
# print(ac.input('#'))
# print(ac.input('i'))
# print(ac.input(' '))
