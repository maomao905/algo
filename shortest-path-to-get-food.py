from typing import List
from collections import deque
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        M,N=len(grid),len(grid[0])
        q = deque()
        for i in range(M):
            for j in range(N):
                if grid[i][j] == '*':
                    q.append((i,j))
                    break
        
        d = 0
        while q:
            d += 1
            for _ in range(len(q)):
                i,j = q.popleft()
                
                for di, dj in ((1,0),(-1,0),(0,-1),(0,1)):
                    _i,_j = i+di,j+dj
                    if 0<=_i<M and 0<=_j<N and grid[_i][_j] in ('O', '#'):
                        if grid[_i][_j] == '#':
                            return d
                        q.append((_i,_j))
                        grid[_i][_j] = 'X'
        return -1

s = Solution()
print(s.getFood([["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]))
print(s.getFood([["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["X","X","X","X","X"]]))
print(s.getFood([["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O","X"],["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["X","X","X","X","X","X","X","X"]]))
print(s.getFood([['O','*'],['#','O']]))
                
        
