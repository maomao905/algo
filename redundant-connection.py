"""
if there is no cycle, it's tree
how can we detect cycle
    - a node is visited twice

start from any point
dfs and when we find node which is visited twice, return the edge index and the node value
the node visited twice get returned value and we

time O(N)
"""

from typing import List
from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for i, e in enumerate(edges):
            graph[e[0]].append((e[1], i))
            graph[e[1]].append((e[0], i))
        
        seen = set()
        ans = 0
        def dfs(n, previous=None):
            if n in seen:
                return n
            
            seen.add(n)
            for m, i in graph[n]:
                if m == previous:
                    continue
                k = dfs(m, n)
                if k:
                    nonlocal ans
                    # print(i, k)
                    ans = max(ans, i)
                    return k if k != n else None
            
            return None
        
        dfs(1)
        return edges[ans]

"""
when we add new edge (a, b), a and b should be disjoint set if it's tree

time O(logN) space O(N)
"""
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = {}
        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        
        def union(x, y):
            uf.setdefault(x, x)
            uf.setdefault(y, y)
            _x = find(x)
            _y = find(y)
            # print((x, _x), (y, _y))
            if _x == _y:
                return False
            
            uf[_x] = _y
            return True
            
        for e in edges:
            if not union(*e):
                return e
                
                
            
s = Solution()
print(s.findRedundantConnection([[1,2],[1,3],[2,3]]))
print(s.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))
