"""
hash the distance from the origin
O(MN)
"""

from typing import List
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(i,j,origin):
            res = [(origin[0]-i,origin[1]-j)]
            grid[i][j] = 0
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                _i,_j = i+di,j+dj
                if 0<=_i<M and 0<=_j<N and grid[_i][_j] == 1:
                    res.extend(dfs(_i,_j,origin))
            return res
        
        M,N=len(grid),len(grid[0])
        seen = set()
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    d = dfs(i,j, (i,j))
                    seen.add(tuple(d))
        return len(seen)

"""
record path
when backtracking, we record backtrack mark to distinguish
"""
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(i,j,direction='s'):
            res = []
            grid[i][j] = 0
            res.append(direction)
            for di,dj,d in ((1,0,'d'),(-1,0,'u'),(0,1,'r'),(0,-1,'l')):
                _i,_j = i+di,j+dj
                if 0<=_i<M and 0<=_j<N and grid[_i][_j] == 1:
                    res.extend(dfs(_i,_j,d))
            res.append('b')
            return res
        
        M,N=len(grid),len(grid[0])
        seen = set()
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    d = dfs(i,j)
                    seen.add(tuple(d))
        # print(seen)
        return len(seen)

s = Solution()
print(s.numDistinctIslands(
[[1,1,0,0,0],
 [1,1,0,0,0],
 [0,0,0,1,1],
 [0,0,0,1,1]]    
))
print(s.numDistinctIslands(
[[1,1,0,1,1],
 [1,0,0,0,0],
 [0,0,0,0,1],
 [1,1,0,1,1]]    
))
print(s.numDistinctIslands(
[[1,1,0],
 [0,1,1],
 [0,0,0],
 [1,1,1],
 [0,1,0]]
))
            
