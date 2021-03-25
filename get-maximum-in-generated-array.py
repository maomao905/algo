"""
time O(NlogN) space O(N)
"""

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        
        memo = [None] * (n+1)
        memo[0] = 0
        memo[1] = 1
        
        def helper(i):
            if memo[i] is None:
                res = 0
                if i % 2:
                    _i = (i-1)//2
                    res = helper(_i) + helper(_i+1)
                else:
                    res = helper(i//2)
                
                memo[i] = res
            return memo[i]
        
        for _n in range(n+1):
            helper(_n)
        return max(memo)

"""
time O(N) space O(N)
"""
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        res = [0] * (n+1)
        res[1] = 1
        for i in range(n+1):
            if i*2 <= n:
                res[i*2] = res[i]
            if i*2+1 <= n:
                res[i*2+1] = res[i] + res[i+1]
        return max(res)

"""
optimized solution
"""
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        res = [0] * (n+1)
        res[1] = 1
        for i in range((n//2)+1):
            res[i*2] = res[i]
            if i*2+1 <= n:
                res[i*2+1] = res[i] + res[i+1]
        return max(res)

s = Solution()
print(s.getMaximumGenerated(7))
print(s.getMaximumGenerated(2))
print(s.getMaximumGenerated(3))
print(s.getMaximumGenerated(4))
