"""
brute-force

generate all two letters for each strs[i]
tars -> {atrs, rats, sart, tras, tsra, tast} -> it takes too much time
if there is a match in set(strs), union them

check all other strs instead O(N)

O(N^2*L) -> 300^3
but once union them, store them in seen, which saves times
"""
from typing import List
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        uf = {}
        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        
        def union(x, y):
            uf.setdefault(x, x)
            uf.setdefault(y, y)
            uf[find(x)] = find(y)
        
        N=len(strs)
        L=len(strs[0])
        for i in range(N):
            s = strs[i]
            uf.setdefault(s, s)
            
            for j in range(i+1,N):
                ss = strs[j]
                if sum(c == cc for c, cc in zip(s, ss)) >= L-2:
                    union(s, ss)
        
        return len(set(find(s) for s in strs))
                    
