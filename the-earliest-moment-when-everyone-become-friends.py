from typing import List
"""
union find
"""

class Solution:
    def earliestAcq(self, logs: List[List[int]], N: int) -> int:
        uf = {}
        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        
        def union(x, y):
            uf.setdefault(x, x)
            uf.setdefault(y, y)
            _x, _y = find(x), find(y)
            uf[_x] = _y
            return _x == _y
            
        remain = N
        for t, a, b in sorted(logs):
            if not union(a, b):
                remain -= 1
            
            if remain == 1:
                return t
        
        return -1

s = Solution()
print(s.earliestAcq(logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], N = 6))
print(s.earliestAcq([[2,2,3],[0,2,0],[1,3,2]], 4))
print(s.earliestAcq([[0,1,0],[4,5,2],[2,4,5],[3,2,0],[1,5,3]], 6))
        
                
        
