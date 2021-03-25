from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N=len(cost)
        dp = [float('inf')]*(N+2)
        dp[0] = dp[1] = 0
        for i in range(N):
            dp[i+1] = min(dp[i+1], dp[i] + cost[i])
            dp[i+2] = min(dp[i+2], dp[i] + cost[i])
        
        return dp[N]

s = Solution()
print(s.minCostClimbingStairs([10,15,20]))
print(s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
