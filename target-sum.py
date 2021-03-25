"""
DP

sum([1,1,1,1,1]) = 5

1+1+1+1-1 = 3 -> (5-3)//2 = 1
get combinations, which sum is 1 -> DP
if we cannot devide, we cannot make the combination

  0 1
1 1 1
1 1 2
1 1 3
1 1 4
1 1 5

time: O(S * N)
space: O(S)
"""

from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        _sum = sum(nums)
        remain = (_sum - S)
        if remain % 2 == 1:
            return 0
        
        target = remain // 2
        if not (0 <= target <= _sum):
            return 0
        
        if target == 0:
            return 2 ** nums.count(0)
        
        dp = [0] * (target + 1)
        
        dp[0] = 1
        dp[nums[0]] += 1
        
        for n in nums[1:]:
            for i in reversed(range(target+1)):
                if i-n >= 0:
                    dp[i] += dp[i-n]
        return dp[-1]

s = Solution()
# print(s.findTargetSumWays([1,1,1,1,1], 3))
print(s.findTargetSumWays([1,0], 1))
print(s.findTargetSumWays([0,0,0,0,0,0,0,0,1],1))
print(s.findTargetSumWays([9,7,0,3,9,8,6,5,7,6],2))
print(s.findTargetSumWays([0,4,6,0,3,2,6,9,4,1],3))
        
        
        
        
