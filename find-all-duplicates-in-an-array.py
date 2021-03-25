"""
mark visited in an input array itself
negate to mark visited
if num appear twice, it turns positive again
we extract the positive ones

time: O(N)
space: O(1)
"""

from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for n in nums:
            nums[abs(n)-1] *= -1
        
        res = []
        for n in nums:
            if nums[abs(n)-1] > 0:
                res.append(abs(n))
                nums[abs(n)-1] *= -1
        return res

s = Solution()
print(s.findDuplicates([4,3,2,7,8,2,3,1]))
