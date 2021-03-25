from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buying = False
        for i in range(len(prices)):
            if buying:
                profit += prices[i] - prices[i-1]
                if i+1 >= len(prices) or prices[i] > prices[i+1]:
                    buying = False
            else:
                if i+1 < len(prices) and prices[i] < prices[i+1]:
                    buying = True
        return profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            p = prices[i] - prices[i-1]
            if p > 0:
                profit += p
        return profit

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
                
