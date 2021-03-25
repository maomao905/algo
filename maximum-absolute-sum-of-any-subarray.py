"""
Kadane's algorithm
both positive and negative

O(N)
"""
from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        mx = mi = cur_mx = cur_mi = 0
        for n in nums:
            cur_mx += n
            if cur_mx > 0:
                mx = max(mx, cur_mx)
            else:
                cur_mx = 0
            
            cur_mi += n
            if cur_mi < 0:
                mi = min(mi, cur_mi)
            else:
                cur_mi = 0
        
        return max(0, mx, -mi)

"""
prefix sum

max min -> remove max to make min sum greater since max >= 0
min max -> remove min to make max sum smaller since min <= 0

O(N)
"""
from itertools import accumulate
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        mx = mi = 0
        for n in accumulate(nums):
            mx = max(mx, n)
            mi = min(mi, n)
        return mx-mi
        
s = Solution()
print(s.maxAbsoluteSum([1,-3,2,3,-4]))
print(s.maxAbsoluteSum([2,-5,1,-4,3,-2]))
            
