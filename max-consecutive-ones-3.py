"""
sliding window
allow zeros of size K in the window

O(N)
"""
from typing import List

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        zeros = 0
        ans = 0
        l = 0
        N=len(A)
        for r in range(N):
            if A[r] == 0:
                zeros += 1
            
            while zeros > K:
                if A[l] == 0:
                    zeros -= 1
                l += 1
            
            ans = max(r-l+1, ans)
        return ans

"""
more efficient approach
our goal is longest length, then we don't need to shrink the window as long as it's already maximum length
"""
class Solution:
    def longestOnes(self, A: List[int], k: int) -> int:
        l = 0
        N=len(A)
        for r in range(N):
            if A[r] == 0:
                k -= 1
            
            if k < 0:
                if A[l] == 0:
                    k += 1
                l += 1
        return N-l

s = Solution()
print(s.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
print(s.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))
