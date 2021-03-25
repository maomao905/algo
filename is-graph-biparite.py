"""
union find
O(α*E)
"""
from typing import List
from collections import defaultdict

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        uf = {}
        def find(x):
            if x not in uf:
                uf[x] = x
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        
        def union(x, y):
            uf.setdefault(x, x)
            uf.setdefault(y, y)
            uf[find(x)] = find(y)
        
        for i, edges in enumerate(graph):
            for j in range(len(edges)):
                union(edges[j], edges[0])
            s = set(find(e) for e in edges)
            if find(i) in s:
                return False
        return True

"""
DFS

color 0 or 1

O(V+E)
"""

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        N=len(graph)
        color = {}
        
        def dfs(i):
            for j in graph[i]:
                if j in color:
                    if color[i] == color[j]:
                        return False
                else:
                    color[j] = 1 - color[i]
                    if not dfs(j):
                        return False
            return True
        
        for i in range(N):
            if i not in color:
                color[i] = 0
                if not dfs(i):
                    return False
        return True
            

s = Solution()
print(s.isBipartite([[1,3],[0,2],[1,3],[0,2]]))
print(s.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))
print(s.isBipartite([[4],[],[4],[4],[0,2,3]]))
assert s.isBipartite([[1],[0],[4],[4],[2,3]]) == True
assert s.isBipartite([[1,2,3,4],[0,2,3,4],[0,1,4],[0,1,4],[0,1,2,3],[6,7,9],[5,7,9],[5,6,8,9],[7,9],[5,6,7,8],[11,12,13],[10,12,13,14],[10,11,13,14],[10,11,12,14],[11,12,13],[16,17],[15,18],[15,19],[16],[17],[22,24],[22,23,24],[20,21],[21],[20,21],[26,27,29],[25,27,28,29],[25,26],[26,29],[25,26,28],[31,32,33,34],[30,32,34],[30,31,33,34],[30,32,34],[30,31,32,33],[37,38,39],[37,38,39],[35,36,38,39],[35,36,37,39],[35,36,37,38],[42,43,44],[42,43,44],[40,41,43,44],[40,41,42],[40,41,42],[48,49],[47,48,49],[46,48,49],[45,46,47,49],[45,46,47,48]]) == False
