"""
O(N sprt(N))
"""
from typing import List
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        last = stones[-1]
        if stones[1] != 1:
            return False
        stones = set(stones)
        memo = {}
        def helper(i, k):
            if i == last:
                return True
            elif i >= last:
                return False
            
            if (i,k) not in memo:
                memo[i,k] = any(helper(i+_k, _k) for _k in (k-1,k,k+1) if _k > 0 and i+_k in stones)
            return memo[i,k]
        
        return helper(1,1)
        
s = Solution()
print(s.canCross([0,1,3,5,6,8,12,17]))
print(s.canCross([0,1,2,3,4,8,9,11]))
print(s.canCross([0,2]))
