"""
greedy

we don't need to dfs to color because we have only 3 colors

O(V+E)
"""
from typing import List

class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        g = [[] for i in range(N)]
        for i,j in paths:
            g[i-1].append(j-1)
            g[j-1].append(i-1)
        
        res = [None] * N
        for i in range(N):
            res[i] = ({1,2,3,4} - set([res[j] for j in g[i]])).pop()
        return res

s = Solution()
print(s.gardenNoAdj(3,[[1,2],[2,3],[3,1]]))
print(s.gardenNoAdj(4,[[1,2],[3,4]]))
print(s.gardenNoAdj(4,[[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]))
            
        
        
