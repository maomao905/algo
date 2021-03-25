from typing import List

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if A[0] == A[-1]:
            check = lambda a, b: a == b
        elif A[0] < A[-1]:
            check = lambda a, b: a <= b
        else:
            check = lambda a, b: a >= b
        
        N=len(A)
        return all(check(A[i-1], A[i]) for i in range(1,N))

            
s = Solution()
print(s.isMonotonic([1,2,2,3]))
