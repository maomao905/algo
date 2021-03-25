"""
O(NLlogNL)
"""
from typing import List

class Solution:
    def longestWord(self, words: List[str]) -> str:
        seen = set()
        for w in sorted(words, key=len):
            if len(w) == 1:
                seen.add(w)
            elif w[:-1] in seen:
                seen.add(w)
        
        ans = ''
        for w in seen:
            if len(ans) < len(w) or (len(ans) == len(w) and w < ans):
                ans = w
        return ans    

"""
trie
O(NL)
"""
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = {}
        for w in words:
            node = trie
            for c in w:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['*'] = w
        
        ans = ''
        def dfs(node):
            for ch in node:
                if '*' in node[ch]:
                    nonlocal ans
                    w = node[ch]['*']
                    if len(ans) < len(w) or (len(ans) == len(w) and w < ans):
                        ans = w
                    dfs(node[ch])
        
        dfs(trie)
        return ans
            
s = Solution()
print(s.longestWord(['w','wo','wor','worl','world']))
print(s.longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"]))
