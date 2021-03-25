"""
DP
"""

from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        dp = [[0] * M for _ in range(N)]
        
        for i in range(N):
            if i == 0:
                dp[i][0] = grid[i][0]
            else:
                dp[i][0] = dp[i-1][0] + grid[i][0]
        
        for j in range(M):
            if j == 0:
                dp[0][j] = grid[0][j]
            else:
                dp[0][j] = dp[0][j-1] + grid[0][j]
        
        for i in range(1, N):
            for j in range(1, M):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]

s = Solution()
print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
        
