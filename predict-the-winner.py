"""
memorization

O(N^2)
"""

from typing import List

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def helper(l,r):
            if l == r:
                return nums[l]
            
            if (l,r) not in memo:
                memo[l,r] = max(nums[l] - helper(l+1, r), nums[r] - helper(l, r-1))
            return memo[l,r]
        
        N=len(nums)
        memo = {}
        return helper(0,N-1) >= 0

s = Solution()
print(s.PredictTheWinner([1,5,2]))
print(s.PredictTheWinner([1,5,233,7]))
print(s.PredictTheWinner([1,2,99]))
            
