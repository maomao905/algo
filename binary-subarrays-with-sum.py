"""
queue
1. expand the window
    if 1:
        add current index to queue
    
    if len(q) == S:
        ans += q[0] - left
    elif len(q) > S:
        i = popleft queue
        l = i+1
        ans += q[0] - left

0 1 0 1 0 1
    ^     ^
"""

from typing import List
from collections import deque
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        N=len(A)
        ans = 0
        l = 0
        q = deque()
        for r in range(N):
            if A[r]:
                q.append(r)
            
            if len(q) > S:
                l = q.popleft() + 1
            
            if len(q) == S and l <= r:
                ans += q[0] - l + 1 if q else r-l+1
                
        return ans

"""
prefix sum
"""
from collections import Counter
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        N=len(A)
        seen = Counter({0:1})
        C = 0
        ans = 0
        for i in range(N):
            C += A[i]
            if C-S in seen:
                ans += seen[C-S]
            seen[C] += 1
        return ans

s = Solution()
print(s.numSubarraysWithSum([1,0,1,0,1],2))
print(s.numSubarraysWithSum([1,0,1,0,1,0],0))
print(s.numSubarraysWithSum([1,1,1,0],3))
print(s.numSubarraysWithSum([0,0,0,0,0],0))
