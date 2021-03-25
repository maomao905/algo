"""
[1,2,3,0,2]

finite state machine
sold: sell a stock
        - held state -> sell action -> sold state
held - owns stock
        - held state -> held state
        - rest state -> buy action -> held state
rest - it does not own stock and do nothing
        - rest state -> rest state
        - sold state -> rest state

maximum value of ith state
sold[i] = held[i-1] + price[i]
held[i] = max(held[i-1], rest[i-1]-price[i])
rest[i] = max(rest[i-1], sold[i-1])

      1  2  3  0  2
sold  0  1  2 -1  3
held  -1 -1 -1 1  1
rest  0  0  1  2  2

max profit = max(sold[-1], rest[-1])
held[-1] will never be the max profit because we will increase the profit if we sell a held stock

time: O(N)
space: O(1)
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        
        sold = [0] * len(prices)
        held = [0] * len(prices)
        rest = [0] * len(prices)
        
        for i in range(len(prices)):
            if i == 0:
                held[i] = -prices[i]
                continue
            
            sold[i] = held[i-1] + prices[i]
            held[i] = max(held[i-1], rest[i-1]-prices[i])
            rest[i] = max(rest[i-1], sold[i-1])
        
        return max(sold[-1], rest[-1])

"""
memorization
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def helper(i, state):
            if i >= N:
                return 0
            
            if (i,state) not in memo:
                m = 0
                if state == 'nothing':
                    # buy or skip
                    m = max(helper(i+1, 'buying') - prices[i], helper(i+1, 'nothing'))
                elif state == 'cooldown':
                    m = helper(i+1, 'nothing')
                elif state == 'buying':
                    # sell or skip
                    m = max(helper(i+1, 'cooldown') + prices[i], helper(i+1, 'buying'))
                
                memo[i,state] = m
            return memo[i,state]
        N=len(prices)
        return helper(0, 'nothing')

s = Solution()
print(s.maxProfit([1,2,3,0,2]))
