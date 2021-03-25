"""
keep track of max up to i-2th index (max_n)
max_n > A[i] -> False
"""
from typing import List

class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        N=len(A)
        max_n = A[0]
        i=2
        while i < N:
            if max_n > A[i]:
                return False
            i += 1
            max_n = max(max_n, A[i-2])
        return True

s = Solution()
print(s.isIdealPermutation([1,0,2]))
print(s.isIdealPermutation([1,2,0]))
print(s.isIdealPermutation([0,2,1]))
print(s.isIdealPermutation([0,2,3,1]))
            
            
            
