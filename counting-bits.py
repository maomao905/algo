"""
Hamming weight

8 & 7 = 0 because 8 == 1000 and n & n-1 excludes the least significant 1 bit then 0000 -> 0's 1bit count + 1

time: O(N)
space: O(N)
"""

from typing import List
class Solution:
    def countBits(self, num: int) -> List[int]:
        
        res = [0] * (num+1)
        for n in range(1, num+1):
            res[n] = res[n & n-1] + 1
        
        return res

s = Solution()
print(s.countBits(2))
print(s.countBits(5))
        
