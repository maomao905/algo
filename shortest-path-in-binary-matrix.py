from typing import List
from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        M,N=len(grid),len(grid[0])
        if grid[0][0] != 0 or grid[M-1][N-1] != 0:
            return -1
        
        q = deque([(0,0)])
        d = 0
        while q:
            d += 1
            for _ in range(len(q)):
                i,j = q.popleft()
                if i == M-1 and j == N-1:
                    return d
                for di, dj in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)):
                    _i,_j = i+di,j+dj
                    if 0<=_i<M and 0<=_j<N and grid[_i][_j] == 0:
                        q.append((_i,_j))
                        grid[_i][_j] = 1
        return -1

s = Solution()
print(s.shortestPathBinaryMatrix([[0,1],[1,0]]))
print(s.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))
                
