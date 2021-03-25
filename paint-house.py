"""
ith house jth color

dp[i][green] = dp[i-2] + min(c[i-1][blue], c[i-1][red]) + c[i][green]
dp[i][blue] = dp[i-2] + min(c[i-1][green], c[i-1][red]) + c[i][blue]
dp[i][red] = dp[i-2] + min(c[i-1][blue], c[i-1][green]) + c[i][red]
dp[i] = min(dp[i][green], dp[i][blue], dp[i][red])

dp[0] = min(c[0])
dp[1] = remove dp[i-2] from above

time: O(N)
space: O(1) -> we only keep dp[i-2]
"""
from typing import List
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs) == 0:
            return 0
        
        green,blue,red = 0,1,2
        prev = costs[0]
        for i in range(1, len(costs)):
            g = min(prev[blue], prev[red]) + costs[i][green]
            b = min(prev[green], prev[red]) + costs[i][blue]
            r = min(prev[green], prev[blue]) + costs[i][red]
        
            prev = [g, b, r]
        
        return min(prev)

s = Solution()
print(s.minCost([[17,2,17],[16,16,5],[14,3,19]]))
print(s.minCost([]))
print(s.minCost([[7,6,2]]))
print(s.minCost([[5,8,6],[19,14,13],[7,5,12],[14,15,17],[3,20,10]]))
