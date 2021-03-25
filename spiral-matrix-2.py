from typing import List
class Solution:
    def generateMatrix(self, N: int) -> List[List[int]]:
        g = [[None]*N for _ in range(N)]
        
        last = N**2
        def fill(i,j, n, dir):
            _i,_j = 0,0
            while 0 <= i < N and 0 <= j < N and g[i][j] is None:
                g[i][j] = n
                _i,_j = i,j
                if n == last:
                    return
                i,j = i+dir[0],j+dir[1]
                n += 1
            
            if dir == (0,1):
                dir = (1,0)
            elif dir == (1,0):
                dir = (0,-1)
            elif dir == (0,-1):
                dir = (-1,0)
            else:
                dir = (0,1)
            
            fill(_i+dir[0],_j+dir[1],n,dir)
        
        fill(0,0,1,(0,1))
        return g

"""
simpler solution

1. di,dj -> dj,-di
(0,1) -> (1,0)
(1,0) -> (0,-1)
(0,-1) -> (-1,0)
(-1,0) -> (0,1)

2. if grid[i%n], there is a number in the cell already
"""

class Solution:
    def generateMatrix(self, N: int) -> List[List[int]]:
        g = [[0]*N for _ in range(N)]
        
        last = N**2
        n = 1
        i,j = 0,0
        di,dj = 0,1
        
        while n <= last:
            g[i][j] = n
            
            if g[(i+di)%N][(j+dj)%N]:
                di,dj = dj,-di
            
            i += di
            j += dj
            n += 1
        return g

s = Solution()
print(s.generateMatrix(3))
print(s.generateMatrix(1))
