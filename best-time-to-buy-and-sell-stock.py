from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buying_price = float('inf')
        
        for p in prices:
            if p < buying_price:
                buying_price = p
            else:
                max_profit = max(max_profit, p - buying_price)
        
        return max_profit
        
s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([7,6,4,3,1]))
