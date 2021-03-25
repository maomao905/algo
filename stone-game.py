"""
brute force O(2^n)
memorization O(n^2)
"""
from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        def helper(l,r):
            if l==r:
                return 0
            
            if (l,r) not in memo:
                memo[l,r] = max(piles[l] - helper(l+1,r), piles[r] - helper(l,r-1))
            return memo[l,r]
        
        N=len(piles)
        memo = {}
        return helper(0,N-1) > 0

"""
Alex can always take the first, third...
"""
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True

s = Solution()
print(s.stoneGame([5,3,4,5]))
print(s.stoneGame([5,7,6,5]))
