"""
xor twice -> 0
xor once -> remain
"""

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        r = 0
        for n in nums:
            r ^= n
        
        for n in range(len(nums)+1):
            r ^= n
        
        return r

s = Solution()
print(s.missingNumber([3,0,1]))
print(s.missingNumber([0]))
