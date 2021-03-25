"""
bit manipulation

appear once        -> seen_once is 1
appear three times -> seen_once is 0

first time -> seen_once changes
    ~seen_twice = 1 seen_once^n = 1
    seen_once = 1 & 1 = 1
    ~seen_once = 0 seen_twice^n = 1
    seen_twice = 0 & 1 = 0
second time -> seen_once becomes 0 and seen_twice changes
    ~seen_twice = 1 seen_once^n = 0
    seen_once = 1 & 0 = 0
    ~seen_once = 1 seen_twice^n = 1
    seen_twice = 1 & 1 = 1
third times -> seen_once stays 0 and seen_twice becomes 0
    ~seen_twice = 0 seen_once^n = 1
    seen_once = 0 & 1 = 0
    ~seen_once = 1 seen_twice^n = 0
    seen_twice = 1 & 0 = 0
"""

from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_once = seen_twice = 0
        for n in nums:
            # change only if seen_twice is 0
            seen_once = ~seen_twice & (seen_once^n)
            # change only if seen_once is 0 (when number appears second times)
            seen_twice = ~seen_once & (seen_twice^n)
        
        return seen_once

s = Solution()
s.singleNumber([2,2,2])
# s.singleNumber([0,1,0,1,0,1,99])
