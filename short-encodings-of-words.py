"""
check if last character exits in trie
if it exists, ans - len(w)
if not, ans + len(w)

O(NL)
"""
from typing import List

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        ans = 0
        trie = {}
        for w in words:
            node = trie
            for c in reversed(w):
                if c not in node:
                    node[c] = {}
                if '*' in node:
                    ans -= node.pop('*')
                node = node[c]
            # the end character is new
            if not node:
                node['*'] = len(w) + 1
                ans += len(w) + 1
        
        return ans

s = Solution()
print(s.minimumLengthEncoding(['time', 'me', 'bell']))
print(s.minimumLengthEncoding(['me', 'time']))
print(s.minimumLengthEncoding(['t']))
