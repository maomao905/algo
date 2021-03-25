"""
union find

- +1 for new land
- ajacent islands -1 if it's not seen
    - keep track of the route of the union in seen hashset
- ignore ajacent islands if it's seen
    - it's already connected

O(k * mn)
"""
from typing import List
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf = {}
        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        
        def union(x, y, seen):
            uf.setdefault(x, x)
            uf.setdefault(y, y)
            _y = find(y)
            uf[find(x)] = _y
            r = _y not in seen
            seen.add(_y)
            return int(r)
        
        res = [1] * len(positions)
        lands = set()
        for idx, (i, j) in enumerate(positions):
            if (i,j) in lands:
                res[idx] = res[idx-1]
                continue
            
            seen = set()
            res[idx] += (res[idx-1] if idx-1>=0 else 0)
            for di, dj in (0,1),(0,-1),(1,0),(-1,0):
                _i,_j = i+di, j+dj
                if 0<=_i<m and 0<=_j<n and (_i,_j) in lands:
                    res[idx] -= union((i,j), (_i,_j), seen)
                lands.add((i,j))
        return res

s = Solution()
print(s.numIslands2(3,3,[[0,0],[0,1],[1,2],[2,1]]))
print(s.numIslands2(3,3,[[0,0],[0,1],[1,2],[1,2]]))
            
        
