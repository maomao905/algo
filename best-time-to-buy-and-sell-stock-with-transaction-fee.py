"""
DP

state:
nothing/buying

action
when nothing, buy or skip
when buying, sell or skip

O(N)
"""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        N=len(prices)
        
        nothing, buying = 'nothing', 'buying'
        def helper(i, state):
            if i >= N:
                return 0
            
            if (i,state) not in memo:
                m = 0
                if state == nothing:
                    m = max(helper(i+1, buying) - prices[i], helper(i+1, nothing))
                else:
                    # buying
                    m = max(helper(i+1, nothing) + prices[i] - fee, helper(i+1, buying))
                memo[i,state] = m
            return memo[i,state]
        
        memo = {}
        return helper(0, nothing)

"""
bottom up 
"""
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        N=len(prices)
        nothing, buying = [0] * N, [0] * N
        buying[0] = -prices[0]
        for i in range(1,N):
            nothing[i] = max(nothing[i-1], buying[i-1]+prices[i]-fee)
            buying[i] = max(nothing[i-1]-prices[i], buying[i-1])
        
        return nothing[-1]

s = Solution()
print(s.maxProfit([1,3,2,8,4,9], 2))
            
            
                
