from typing import List
"""
DP
coin=M
A=amount
use fewest number of coin -> save fewest number in DP table

-> we need only one row to represent dp table
if Coin > Amount: dp[amount] = dp[amount] # same
else: dp[amount] = dp[Amount-Coin]+1

  0  1 2 3 4 5 6 7 8 9 10 11
1 0  1 2 3 4 5 6 7 8 9 10 11 
2 0  1 1 2 2 3 3 4 4 5 5  6
5 0  1 1 2 2 1 2 2 3 3 2  3

time: O(MA)
space: O(A)
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        
        for coin in coins:
            for amount in range(coin,amount+1):
                dp[amount] = min(dp[amount], dp[amount-coin] + 1)
        
        return dp[-1] if dp[-1] < float('inf') else -1

s = Solution()
print(s.coinChange([1,2,5], 11))
print(s.coinChange([2], 3))
print(s.coinChange([1], 0))
print(s.coinChange([1], 1))
print(s.coinChange([1], 2))
