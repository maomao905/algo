"""
(TLE)
DFS

O(N^2)
"""

from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        unsafe = set()
        seen = set()
        def dfs(i):
            if i in seen:
                unsafe.add(i)
                return False
            
            seen.add(i)
            for j in graph[i]:
                if not dfs(j):
                    unsafe.add(j)
                    return False
            
            seen.discard(i)
            return True
        
        return [i for i in range(len(graph)) if dfs(i)]

"""
topological sort
start from terminal node
remove edges to terminal node
find next terminal node

O(V+E) V: number of nodes
"""
from collections import deque, defaultdict, Counter
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        parents = defaultdict(list)
        out_degrees = Counter()
        q = deque()
        N=len(graph)
        for i in range(N):
            for p in graph[i]:
                parents[p].append(i)
            out_degrees[i] = len(graph[i])
            if out_degrees[i] == 0:
                q.append(i)
        
        safe = [False] * N
        while q:
            i = q.popleft()
            safe[i] = True
            for j in parents[i]:
                out_degrees[j] -= 1
                if out_degrees[j] == 0:
                    q.append(j)
        return [i for i in range(N) if safe[i]]

s = Solution()
print(s.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))
print(s.eventualSafeNodes([[1,2,3,4],[1,2],[3,4],[0,4],[]]))
            
