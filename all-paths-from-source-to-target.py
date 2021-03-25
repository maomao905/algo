"""
DFS

repeat to decide source, destination node until reaching n

BFS
putting next node into queue
pop until queue become empty

time: O(2^N *N)
space: O(N)
"""
from typing import List
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(path, s):
            if s == n:
                res.append(list(path))
            
            for d in graph[s]:
                path.append(d)
                dfs(path, d)
                # backtrack
                path.pop()
        
        n = len(graph)-1
        res = []
        dfs([0], 0)
        return res

s = Solution()
print(s.allPathsSourceTarget([[1,2],[3],[3],[]]))
print(s.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))
