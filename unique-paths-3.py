"""
1. make sure the path reaches the goal
    - DFS
    - 3^N
2. visit exactly once
    - keep track of visited square
    - len(visited) == N at the goal
    
time O(3^N)
space O(N) N is the total number of cells
"""

from typing import List
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if grid[i][j] == 2:
                return int(len(seen)+1 == M * N)
            
            seen.add((i,j))
            res = 0
            for di, dj in ((0,1),(0,-1),(1,0),(-1,0)):
                _i = i + di
                _j = j + dj
                if 0 <= _i < M and 0 <= _j < N and (_i,_j) not in seen:
                    res += dfs(_i,_j)
            
            seen.remove((i,j))
            return res
        
        def get_start():
            start = None
            for i in range(M):
                for j in range(N):
                    if grid[i][j] == 1:
                        start = (i,j)
                    if grid[i][j] == -1:
                        seen.add((i,j))
            return start
                    
        seen = set()
        M,N=len(grid),len(grid[0])
        i,j = get_start()
        return dfs(i,j)

s = Solution()
print(s.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))
