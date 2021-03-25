"""
union-find

O(V + ElogE) V:vertices E:edges
"""
from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = {}
        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        
        def union(x, y):
            uf.setdefault(x, x)
            uf.setdefault(y, y)
            uf[find(x)] = uf[find(y)]
        
        for x, y in edges:
            union(x, y)
        
        # already find(x) during union, so it's O(N) per find(x)
        return len(set(find(x) for x in uf)) + n - len(uf)

"""
DFS
O(V+E)
"""
from collections import defaultdict
class Solution:
    def countComponentsDFS(self, n: int, edges: List[List[int]]) -> int:
        def dfs(x):
            if x in seen:
                return
            seen.add(x)
            for y in g[x]:
                dfs(y)
            
        seen = set()
        ans = 0
        g = defaultdict(list)
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        
        for x in g:
            if x not in seen:
                dfs(x)
                ans += 1
        return ans + n - len(g)

"""
performance check
"""
from collections import defaultdict, Counter
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        cnt = 0
        uf = {}
        def find(x):
            nonlocal cnt
            cnt += 1
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        
        def union(x, y):
            uf.setdefault(x, x)
            uf.setdefault(y, y)
            uf[find(x)] = uf[find(y)]
        
        for x, y in edges:
            union(x, y)
        
        print(n, cnt, cnt//n)
        return len(set(find(x) for x in uf)) + n - len(uf)
    
    def countComponentsRank(self, n: int, edges: List[List[int]]) -> int:
        cnt = 0
        uf = {}
        rank = Counter()
        def find(x):
            nonlocal cnt
            cnt += 1
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        
        def union(x, y):
            uf.setdefault(x, x)
            uf.setdefault(y, y)
            x = find(x)
            y = find(y)
            if rank[x] < rank[y]:
                uf[x] = y
            else:
                uf[y] = x
                if rank[x] == rank[y]:
                    rank[x] += 1
        
        for x, y in edges:
            union(x, y)
        
        print(n, cnt, cnt//len(edges))
        return len(set(find(x) for x in uf)) + n - len(uf)
    
    def countComponentsDFS(self, n: int, edges: List[List[int]]) -> int:
        cnt = 0
        def dfs(x):
            nonlocal cnt
            cnt += 1
            if x in seen:
                return
            seen.add(x)
            for y in g[x]:
                dfs(y)
            
        seen = set()
        ans = 0
        g = defaultdict(list)
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        
        for x in g:
            if x not in seen:
                dfs(x)
                ans += 1
        print(n, cnt, cnt//len(edges))
        return ans + n - len(g)

s = Solution()
# print(s.countComponentsRank(5, [[0,1],[1,2],[3,4]]))
# print(s.countComponentsRank(5, [[0,1],[1,2],[2,3],[3,4]]))
# print(s.countComponentsRank(5, [[1,2],[2,3],[3,4]]))
"""
UF 
20 756 37
400 319196 797
8000 127983996 15997
DFS
20 381
400 159601 2 
8000 63992001 2
"""
import sys
sys.setrecursionlimit(10**8)
for i in (20,400,8000):
    N=i
    edges = []
    for i in range(N):
        for j in range(i+1, N):
            edges.append([i,j])
    s.countComponentsDFS(N,edges)
