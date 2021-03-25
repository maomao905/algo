"""
dynamic programming
current path = dp[i-1] + dp[j-1]
if there is a block in i-1 or j-1, i-1 or j-1 path would be zero
time: O(MN)
space: O(1)
"""
from typing import List
class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # block, thus it should stay zero
                if grid[row][col] == 1:
                    grid[row][col] = 0
                    continue
                
                if row == 0 and col == 0:
                    grid[row][col] = 1
                    continue
                
                # add path from previous row
                if row > 0:
                    grid[row][col] += grid[row-1][col]
                
                # add path from previous column
                if col > 0:
                    grid[row][col] += grid[row][col-1]
                
        return grid[-1][-1]

s = Solution()
print(s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
print(s.uniquePathsWithObstacles([[0,1],[0,0]]))
print(s.uniquePathsWithObstacles([[0,0],[0,1]]))
                
        
