"""
memorization
time O(DT) space O(DT)
D: num of dice T: target
"""

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        MOD = 10**9 + 7
        def helper(i, remain):
            if i == d and remain == 0:
                return 1
            
            if remain < 0 or i >= d:
                return 0
            
            if (i, remain) not in memo:
                memo[i, remain] = sum(helper(i+1, remain-n) for n in range(1,f+1)) % MOD
            return memo[i, remain]
        
        memo = {}
        return helper(0, target)

s = Solution()
print(s.numRollsToTarget(1,6,3))
print(s.numRollsToTarget(2,6,7))
print(s.numRollsToTarget(2,5,10))
print(s.numRollsToTarget(1,2,3))
print(s.numRollsToTarget(30,30,500))
