"""
if i,j face boundary, return 0, otherwise return 1

to avoid dfs loop, keep track of visited cells

if seen[i,j] = -1, current dfs, return 1
if seen[i,j] = 0, it leads to boundary, return 0
if seen[i,j] = 1, it's closed island, return 1
"""

from typing import List
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if i in (0,M-1) or j in (0,N-1):
                seen[i,j] = 0
                return 0
            
            if (i,j) in seen:
                if seen[i,j] == -1:
                    return 1
                else:
                    return seen[i,j]

            
            seen[i,j] = -1
            
            seen[i,j] = int(all(dfs(i+di,j+dj) for di,dj in ((1,0),(-1,0),(0,-1),(0,1)) if grid[i+di][j+dj] == 0))
            return seen[i,j]
                
        
        seen = {}
        M,N=len(grid),len(grid[0])
        ans = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0 and (i,j) not in seen:
                    ans += dfs(i,j)
        return ans

"""
simpler DFS
flood fill algorithm

O(N)
"""
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            grid[i][j] = 1
            for di, dj in ((1,0),(-1,0),(0,-1),(0,1)):
                _i,_j = i+di,j+dj
                if 0<=_i<M and 0<=_j<N and grid[_i][_j] == 0:
                    dfs(_i,_j)
                
        
        M,N=len(grid),len(grid[0])
        for i in range(M):
            if i in (0,M-1):
                for j in range(N):
                    if grid[i][j] == 0:
                        dfs(i,j)
            else:
                for j in (0,N-1):
                    if grid[i][j] == 0:
                        dfs(i,j)
                
        ans = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0:
                    dfs(i,j)
                    ans += 1
        return ans

s = Solution()
print(s.closedIsland([[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]))
print(s.closedIsland([[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]))
print(s.closedIsland([[0,1,1,1,1,1,1,1],[1,0,1,0,0,0,0,1],[1,0,0,0,0,1,0,1],[0,1,0,0,0,1,0,1],[1,0,0,1,0,1,0,1],[1,1,1,1,0,0,1,1],[1,0,0,0,0,0,1,1],[0,1,1,1,1,1,1,1]]))
print(s.closedIsland([[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]))
