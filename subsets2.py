"""
backtrack
skip same number

O(N*2^N)
"""
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        N=len(nums)
        def recursive(i, comb=[]):
            res.append(list(comb))
            
            for j in range(i, N):
                # count only one time (only when i == j)
                if i != j and nums[j] == nums[j-1]:
                    continue
                comb.append(nums[j])
                recursive(j+1, comb)
                comb.pop()
        
        nums.sort()
        recursive(0)
        return res

s = Solution()
print(s.subsetsWithDup([1,2,2]))
