from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j):
            grid[i][j] = 0
            for di, dj in ((0,1),(0,-1),(-1,0),(1,0)):
                _i,_j = i+di,j+dj
                if 0<=_i<M and 0<=_j<N and grid[_i][_j] == "1":
                    dfs(_i,_j)

        M,N = len(grid), len(grid[0])

        ans = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i, j)
        return ans
