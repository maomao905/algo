"""
(WA)
wordlist = ['kite']
possible queries
kata
 i i
 u u
 e e
 o o

build trie of wordlist
for char in node:
    the char matches if the char and query char is same or capital, the char is vowel and query char is vowel
"""
from typing import List
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        word_idx = {w: i for i, w in enumerate(wordlist)}
        def build_trie():
            trie = {}
            for w in wordlist:
                node = trie
                for c in w:
                    if c not in node:
                        node[c] = {}
                    node = node[c]
                node['*'] = w
            return trie
        
        vowels = set(['a', 'i', 'u', 'e', 'o'])
        def dfs(q, i, node):
            if i == len(q):
                return (0, node['*']) if '*' in node else (3, '')
            
            res = (3, '')
            for c in node:
                rank = -1
                if c == q[i]:
                    rank = 0
                elif c.lower() == q[i].lower():
                    rank = 1
                elif q[i].lower() in vowels and c in vowels:
                    rank = 2
                else:
                    continue
                
                _rank, w = dfs(q, i+1, node[c])
                if not w:
                    continue
                
                if not res[1] or rank < res[0] or (res[0] == rank and word_idx[res[1]] > word_idx[w]):
                    res = (rank, w)
            return res
        
        
        res = []
        trie = build_trie()
        for q in queries:
            res.append(dfs(q, 0, trie)[1])
        return res

"""
hashmap for all cases
"""

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def vowel(w):
            return ''.join('*' if c in {'a', 'i', 'u', 'e', 'o'} else c for c in w)
            
        d = set()
        lower_d = {}
        vowel_d = {}
        for w in wordlist:
            d.add(w)
            _w = w.lower()
            if _w not in lower_d:
                lower_d[_w] = w
            _w = vowel(_w)
            if _w not in vowel_d:
                vowel_d[_w] = w
        
        def search(q):
            if q in d:
                return q
            q = q.lower()
            return lower_d.get(q) or vowel_d.get(vowel(q)) or ''
        
        return list(map(search, queries))
        

s = Solution()
print(s.spellchecker(wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]))
