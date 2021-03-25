"""
DP (knapsack problem)
[1,5,11,5] -> [1,5,5], [11]
if odd sum, we cannot partition
even if even sum, we cannot partition in some cases
    - [1,1,1,1,100]

num\sum 0 1 2 3 4 5 6 7 8 9 10 11
  1     1 1 0 0 0 0 0 0 0 0 0  0
  5     1 1 0 0 0 1 1 0 0 0 0  0
  11    1 1 0 0 0 1 1 0 0 0 0  1
  5     1 1 0 0 0 1 1 0 0 0 1  1

compress dp table into one row

time: O(N*S) S=sum
space: O(S)
"""
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        _sum = sum(nums)
        if _sum % 2 == 1:
            return False
        
        target_sum = _sum // 2
        if max(nums) > target_sum:
            return False
        
        dp = [False] * (target_sum + 1)
        
        dp[0] = dp[nums[0]] = True
        
        for n in nums[1:]:
            for i in reversed(range(target_sum + 1)):
                if i >= n:
                    dp[i] = dp[i] or dp[i-n]
        
        return dp[-1]

s = Solution()
# print(s.canPartition([1,5,11,5]))
# print(s.canPartition([1,2,3,5]))
print(s.canPartition([2,2,3,5]))
print(s.canPartition([100,1,1]))
