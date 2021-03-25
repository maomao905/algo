"""
binary search

max of divisor is max(nums) because len(nums) <= threshold
min of divisor is sum(nums)/threshold
    - sum(nums)/D <= threshold
      sum(nums)   <= D * threshold
      sum(nums)/threshold <= D

time Nlog(max of nums) space O(1)
"""

from typing import List
import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def quo(div):
            return sum(math.ceil(n/div) for n in nums)
            
        l = max(sum(nums)//threshold, 1)
        r = max(nums)
        
        while l < r:
            mid = l + (r-l)//2
            if quo(mid) > threshold:
                l = mid + 1
            else:
                r = mid
        return l

s = Solution()
print(s.smallestDivisor([1,2,5,9],6))
print(s.smallestDivisor([44,22,33,11,1],5))
print(s.smallestDivisor(nums = [21212,10101,12121], threshold = 1000000))
print(s.smallestDivisor(nums = [2,3,5,7,11], threshold = 11))
            
            
        
