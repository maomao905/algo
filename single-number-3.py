"""
first-pass
xor -> find number which appear odd times
but we get two numbers which appear once

get the right-most 1 bit from xor result
if the answer is a and b, a or b has the right-most 1bit
let's take the second pass to know which a or b has the right-most 1bit
time: O(N) space: O(1)
"""

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # first pass
        xor = 0
        for n in nums:
            xor ^= n
        
        """
        difference between a and b if a and b are the answer
        because a and b is unique, there is a difference, and we get the right-most difference
        consider diff is a's right-most 1 bit
        """
        diff = xor & -xor
        
        # second pass
        a = 0
        for n in nums:
            """
            diff & a must be greater than 0, since it's rightmost bit is same
            diff & b must be zero, since rightmost bit does't match
            """
            if diff & n:
                a ^= n
        
        # just taking xor again to offset a
        return [a, a^xor]

s = Solution()
print(s.singleNumber([1,2,1,3,2,5]))
