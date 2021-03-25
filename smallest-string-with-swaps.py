"""
graph (union find)

- think of pairs as connected component
    - if pairs contain [1,2],[0,2], we can swap any of [0,1,2]
- sort strings within the same connected component

O(NlogN) space O(N)
"""
from typing import List
from collections import defaultdict
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        if not pairs:
            return s
        
        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        
        def union(x, y):
            uf[find(x)] = find(y)
        
        N=len(s)
        uf = {i: i for i in range(N)}
        for i, j in pairs:
            union(i,j)
        
        swaps = defaultdict(list)
        for i in range(N):
            swaps[find(i)].append(i)
        
        res = [None] * N
        for indexes in swaps.values():
            chars = [s[i] for i in indexes]
            for i, c in zip(sorted(indexes), sorted(chars)):
                res[i] = c
        
        return ''.join(res)

s = Solution()
print(s.smallestStringWithSwaps('dcab', [[0,3],[1,2]]))
print(s.smallestStringWithSwaps('dcab', [[0,3],[1,2],[0,2]]))
print(s.smallestStringWithSwaps('cab', [[0,1],[1,2]]))
print(s.smallestStringWithSwaps('cab', [[0,1]]))
            
