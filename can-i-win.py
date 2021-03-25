"""
try all choices

without memorization time O(maxChoosableInteger ^ sqrt(desiredTotal)) space O(sqrt(desiredTotal))
with memorization time O((2^maxChoosableInteger)*maxChoosableInteger)
"""

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        def helper(choices, remain):
            if remain <= 0:
                return False
            
            fs = frozenset(choices)
            if fs not in memo:
                memo[fs] = any(not helper(choices - set([i]), remain - i) for i in choices)
            
            return memo[fs]
        
        memo = {}
        # impossible to make desiredTotal
        if (1+maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False
        if desiredTotal == 0:
            return True
        return helper(set(range(1,maxChoosableInteger+1)), desiredTotal)

s = Solution()
print(s.canIWin(10,11))
print(s.canIWin(10,0))
print(s.canIWin(10,1))
print(s.canIWin(5,50))
# print(s.canIWin(18,79))
