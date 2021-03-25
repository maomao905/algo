from typing import List

class Solution:
    def longestMountain(self, A: List[int]) -> int:
        N=len(A)
        if N < 3:
            return 0
        
        ans = 0
        i = 0
        start = -1
        while i<N-1:
            # peak found
            if i > 0 and A[i-1] < A[i] > A[i+1]:
                # find the end
                while i+1 < N and A[i] > A[i+1]:
                    i += 1
                ans = max(ans, i - start + 1)
                continue
            
            # update start
            if (i==0 and A[i]<A[i+1]) or (0<i and A[i-1] >= A[i] < A[i+1]):
                start = i
            i += 1
        return ans

s = Solution()
print(s.longestMountain([2,1,4,7,3,2,5]))
print(s.longestMountain([2,2,2]))
print(s.longestMountain([2,3,2]))
print(s.longestMountain([2,2,3,2,2]))
            
            
