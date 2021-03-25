"""
DP
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        n_1 = 1
        n_2 = 0
        ans = 0
        for i in range(n):
            ans = n_2 + n_1
            n_1, n_2 = ans, n_1
        
        return ans

s = Solution()
print(s.climbStairs(2))
print(s.climbStairs(3))
