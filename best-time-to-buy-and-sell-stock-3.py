"""
DP

state
- nothing
    - buy or skip
- buying
    - sell or skip

action
- buy
- sell

time O(N)
"""

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        nothing, buying = 'nothing', 'buying'
        def helper(i, state, remain):
            if i >= N or remain == 0:
                return 0
            
            if (i,state,remain) not in memo:
                m = 0
                if state == nothing:
                    m = max(helper(i+1, buying, remain) - prices[i], helper(i+1, nothing, remain))
                else:
                    # buying
                    m = max(helper(i+1, nothing, remain-1) + prices[i], helper(i+1, buying, remain))
                memo[i,state,remain] = m
            return memo[i,state,remain]
        
        memo = {}
        N=len(prices)
        return helper(0, nothing, 2)
            
s = Solution()            
print(s.maxProfit([3,3,5,0,0,3,1,4]))
print(s.maxProfit([1,2,3,4,5]))
print(s.maxProfit([7,6,4,3,1]))
print(s.maxProfit([1]))
        
