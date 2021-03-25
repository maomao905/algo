"""
- how to get the number of 1 bit?
get right-most 1 bit and substruct it 
continue this process until the number becomes zero O(32) = O(1)

time: O(NlogN) space: O(1)
"""

from typing import List
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def count_one_bit(x):
            cnt = 0
            while x > 0:
                # rightmost_one_bit = x & -x
                # x -= rightmost_one_bit
                x &= (x-1)
                cnt += 1
            return cnt
        
        return sorted(arr, key=lambda x: (count_one_bit(x), x))

s = Solution()
print(s.sortByBits([0,1,2,3,4,5,6,7,8]))
print(s.sortByBits([1024,512,256,128,64,32,16,8,4,2,1]))
print(s.sortByBits([2,3,5,7,11,13,17,19]))
