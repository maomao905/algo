"""
DP
"""
from typing import List

class Solution:
    def longestLine(self, g: List[List[int]]) -> int:
        if not g:
            return 0
        
        M,N=len(g),len(g[0])
        
        ans = 0
        # horizontal, vertical, diagonal,anti-diagonal
        dp = [[[0,0,0,0] for _ in range(N+2)] for _ in range(M+2)]
        for i in range(1,M+1):
            for j in range(1,N+1):
                if g[i-1][j-1] == 0:
                    continue
                dp[i][j][0] = dp[i][j-1][0] + 1
                dp[i][j][1] = dp[i-1][j][1] + 1
                dp[i][j][2] = dp[i-1][j-1][2] + 1
                dp[i][j][3] = dp[i-1][j+1][3] + 1
                ans = max(max(dp[i][j]), ans)
        return ans

s = Solution()
print(s.longestLine(
[[0,1,1,0],
 [0,1,1,0],
 [1,0,0,0]]))
print(s.longestLine(
[[0,1,0,1,1],
 [1,1,0,0,1],
 [0,0,0,1,0],
 [1,0,1,1,1],
 [1,0,0,0,1]]
))
        
