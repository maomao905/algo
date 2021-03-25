"""
1 2 3 4 5
1 2 3 4
  2 3 4    2ways
1 2 3 4 5
  2 3 4 5
    3 4 5  3ways dp[i-1] + 1

base case: start from i = 2, and initialize dp[i] = 0

if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
    dp[i] = dp[i-1] + 1

answer = sum(dp)

O(N)
"""
from typing import List

class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        N=len(A)
        if N<3:
            return 0
        
        dp = [0] * N
        
        for i in range(2,N):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp[i] = dp[i-1] + 1
        return sum(dp)

s = Solution()
print(s.numberOfArithmeticSlices([1,2,3,4]))
print(s.numberOfArithmeticSlices([1,3,5,7,9,10]))
print(s.numberOfArithmeticSlices([7,7,7,7,5,3]))
        
        
        
