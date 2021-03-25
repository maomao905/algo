"""
(WA)
N: length of s
D: size of dictionary

O(2^N)
"""
from typing import List

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        def build_trie():
            trie = {}
            for w in d:
                node = trie
                for c in w:
                    if c not in node:
                        node[c] = {}
                    node = node[c]
                node['*'] = w
            return trie
        
        def update_ans(ans, w):
            if len(ans) > len(w):
                return ans
            elif len(ans) < len(w):
                return w
            else:
                return w if ans > w else ans
        
        trie = build_trie()
        
        ans = ''
        seen = {trie}
        for c in s:
            # dict is not hashable, we cannot add to set
            cur = set()
            for node in seen:
                if c in node:
                    node = node[c]
                    if '*' in node:
                        w = node['*']
                        ans = update_ans(ans, w)
                    cur.add(node)
            seen |= cur
        return ans

"""
pointers

move pointer to right of dictionary if matched

keep {char: [dictionary indices]}
update if s[i] == char

the point is we don't need to go back index if matched, only move forward
O(N+DL)
"""
from collections import defaultdict
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        def update_ans(ans, w):
            if len(ans) > len(w):
                return ans
            elif len(ans) < len(w):
                return w
            else:
                return w if ans > w else ans
        
        cur = defaultdict(list) # char: (index of d, index of word)
        
        for i, w in enumerate(d):
            cur[w[0]].append((i,0))
        
        ans = ''
        for c in s:
            if c in cur:
                matched = cur[c]
                del cur[c]
                
                for i,j in matched:
                    j += 1
                    if j == len(d[i]):
                        ans = update_ans(ans, d[i])
                    else:
                        cur[d[i][j]].append((i,j))
        return ans

s = Solution()
print(s.findLongestWord('abpcplea', ['ale','apple','monkey','plea']))
print(s.findLongestWord('abpcpmleoankey', ['ale','apple','monkey','plea']))
print(s.findLongestWord('abpcplea', ['a','b','c']))
print(s.findLongestWord('a', []))
            
