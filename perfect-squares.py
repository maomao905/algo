"""
DP: recusrsion + memorization
try all possible square recursively

12
3^2 < 12 < 4^2

3^2 + 3
    + 1^2 + 2
          + 1^2 + 1^2
2^2 + 8
    + 2^3
1^2 + 11
    + 3^2 + 2
          + 1^2 + 1^2

time: O(N * sqrt(N))
space: O(N)
"""

import math
class Solution:
    def numSquares(self, n: int, memo={}) -> int:
        if n <= 0:
            return 0
        self.cnt += 1
        if n in memo:
            return memo[n]
        
        i = math.sqrt(n)
        
        if i.is_integer():
            memo[n] = 1
            return 1
        
        res = []
        # loop sqrt(N) times
        for j in range(1,int(i)+1):
            # N times at most
            r = self.numSquares(n-j**2)
            if r > 0:
                res.append(r)
        
        memo[n] = min(res) + 1
        return memo[n]

"""
DP bottom-up

dp[0] = 0
dp[i] = answer of i
dp[i] = min(dp[i-j] for j in sqrt(i))
"""

class Solution:
    def numSquares(self, n):
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        
        _s = int(n**0.5)
        sqrt = [0] * _s
        for i in range(1,_s+1):
            double = i**2
            dp[double] = 1
            sqrt[i-1] = double
        
        # print(sqrt)
        for i in range(1,n+1):
            if dp[i] == 1:
                continue
            j = int(i**0.5)-1
            dp[i] = min(dp[i-_n] for _n in sqrt[:j+1]) + 1
        return dp[-1]

s = Solution()
# print(s.numSquares(3530))
# print(s.numSquares(12))
# print(s.numSquares(13))
print(s.numSquares(28))
# print(s.numSquares(0))
        
        
        
