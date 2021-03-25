"""
permute all cases
"""

from typing import List
from itertools import permutations
class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        ans = ''
        largest = 0
        for A in list(permutations(arr)):
            hour = A[0] * 10 + A[1]
            minute = A[2] * 10 + A[3]
            if 0 <= hour < 24 and 0 <= minute < 60:
                t = hour * 100 + minute
                if t >= largest:
                    largest = t
                    ans = A
            
        if not ans:
            return ''
        
        ans = [str(i) for i in ans]
        return ''.join(ans[:2]) + ':' + ''.join(ans[2:])
        

s = Solution()
print(s.largestTimeFromDigits([1,2,3,4]))
print(s.largestTimeFromDigits([5,5,5,5]))
print(s.largestTimeFromDigits([0,0,0,0]))
print(s.largestTimeFromDigits([9,5,4,2]))
print(s.largestTimeFromDigits([2,0,6,6]))
