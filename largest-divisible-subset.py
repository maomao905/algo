"""
DP

if nums[i] % max(subset) == 0, news[i] can be included
    new element is 8 and current subset [2,4] 
"""

from typing import List
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        N=len(nums)
        memo = {}
        ans = []
        def helper(i):
            best = []
            if i not in memo:
                for j in range(i):
                    if nums[i] % nums[j] == 0:
                        subset = helper(j)
                        if len(best) < len(subset):
                            best = subset
                best = list(best)
                best.append(nums[i])
                memo[i] = best
            return memo[i]
        
        return max([helper(i) for i in range(N)], key=len)

s = Solution()
print(s.largestDivisibleSubset([1,2,3]))
                        
                
        
