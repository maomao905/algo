"""
  0   0            0   1
  W   E            W   E
0 E E 0 W 0 E -> 2 E E 3 W 1 E
  0   W            2   W
  E   0            E   1
  W   E            W   E
  0   0            0   1

use stack to accumulate the number of enemy at each row and column
sum the number of enemy of row and column

O(MN)
"""

from typing import List

class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        M,N=len(grid),len(grid[0])
        res = [[0] * N for _ in range(M)]
        
        # accumulate same row
        stack = []
        for i in range(M):
            cur = 0 # current number of enemy
            for j in range(N):
                if grid[i][j] == '0':
                    stack.append((i,j))
                elif grid[i][j] == 'E':
                    cur += 1
                else:
                    # wall
                    while stack:
                        _i,_j = stack.pop()
                        res[_i][_j] += cur
                    cur = 0
            while stack:
                _i,_j = stack.pop()
                res[_i][_j] += cur
        
        stack = []
        # accumulate same column
        for j in range(N):
            cur = 0 # current number of enemy
            for i in range(M):
                if grid[i][j] == '0':
                    stack.append((i,j))
                elif grid[i][j] == 'E':
                    cur += 1
                else:
                    # wall
                    while stack:
                        _i,_j = stack.pop()
                        res[_i][_j] += cur
                    cur = 0
            while stack:
                _i,_j = stack.pop()
                res[_i][_j] += cur
        
        ans = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == '0':
                    ans = max(ans, res[i][j])
        return ans

s = Solution()
print(s.maxKilledEnemies([["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]))
