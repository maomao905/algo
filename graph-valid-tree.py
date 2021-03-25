"""
- it's tree, there must be N nodes and N-1 edges

union-find
2 - 1 - 0
 \ 
  3

- if we have same root node, it's a loop
[1,3] -> both node have root of 2 -> loop
- if node is new, it's ok and just connect

O(V * α(V))
"""

from typing import List
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = {}
        def find(x):
            if x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]
        
        def union(x, y):
            uf.setdefault(x, x)
            uf.setdefault(y, y)
            _x, _y = find(x), find(y)
            if uf[_x] == uf[_y]:
                return False
                
            uf[_x] = _y
            return True
        
        if len(edges) != n-1:
            return False
        
        for x, y in edges:
            valid = union(x, y)
            if not valid:
                return False
        
        return True
        
"""
DFS

it's not DAG
if it's DAG, simply traverse all connected edges and visit nodes and visit the same node again,
cycle is detected

a -> b -> c -> d -> b
a <- b <- c <- d <- b

when you visit a -> b and we don't want to go back b -> a because it's cycle but it's still valid
we want to find the loop when two nodes are not neighbors but cycled

to avoid such loops, we can pass the previously visited node as well and will not visit previous node
but, we don't even have to do this.

we just dfs all nodes as long as it can and to prevent cycle, we return if it's visited node
finally check the length of visited nodes equals the number of nodes
if a -> b -> a, we can mark all nodes as visited
if a -> b, c -> d we are never able to visit c after a -> b
so, visited length is 2 < 4

we can detect the cycle by checking the edge size - 1 == number of node
a -> b -> c -> d -> b
num of edges [a,b][b,c][c,d][d,b] = 4
num of nodes a,b,c,d = 4 

time: O(E + V) -> O(E) because E is V-1
E: build adjacent list
V: visit all nodes
"""
from typing import List
from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        visited = set()
        neigh = defaultdict(list)
        for x, y in edges:
            neigh[x].append(y)
            neigh[y].append(x)
        
        def dfs(node, prev=None):
            # cycle detected
            if node in visited:
                return
            
            visited.add(node)
            for x in neigh[node]:
                dfs(x, node)
        
        dfs(0)
        return len(visited) == n

s = Solution()
print(s.validTree(5, [[0,1], [0,2], [0,3], [1,4]]))
print(s.validTree(5, [[0,1], [1,2], [2,3], [1,3], [1,4]]))
print(s.validTree(4, [[0,1], [2,3]]))
print(s.validTree(1, []))
print(s.validTree(3, [[1,0]]))
print(s.validTree(5, [[0,1],[0,4],[1,4],[2,3]]))
