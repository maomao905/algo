"""
  0
1   -2
 -1
"""
from typing import List
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        M,N=len(grid),len(grid[0])
        dir = {
            1: (0,-1),
            0: (-1,0),
            -2:(0,1),
            -1:(1,0),
        }
        st = {
            0: {},
            1: {1,-2},
            2: {0,-1},
            3: {1,-1},
            4: {-1,-2},
            5: {1,0},
            6: {0,-2},
        }
        
        seen = {}
        def dfs(i,j,prev=None):
            if not(0<=i<M and 0<=j<N):
                return False
            
            n = grid[i][j]
            path = st[n]
            if prev and prev not in path:
                return False
            
            if i == M-1 and j == N-1:
                return True
            
            if (i,j) not in seen:
                seen[i,j] = False
                for exit in path-{prev}:
                    grid[i][j] = 0
                    seen[i,j] |= dfs(i + dir[exit][0], j + dir[exit][1], ~exit) 
                    grid[i][j] = n
            return seen[i,j]
        
        s = grid[0][0]
        return dfs(0,0,None)

s = Solution()
print(s.hasValidPath([[2,4,3],[6,5,2]]))
print(s.hasValidPath([[1,2,1],[1,2,1]]))
print(s.hasValidPath([[1,1,1,1,1,1,3]]))
print(s.hasValidPath([[2],[2],[2],[2],[2],[2],[6]]))
print(s.hasValidPath([[1,1,2]]))
print(s.hasValidPath([[4,1],[6,1]]))
            
            
