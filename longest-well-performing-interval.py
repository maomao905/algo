"""
prefix sum

1. convert array by 1 if hours > 8 else -1
2. we want such subarray that subarray sum is 1 because 1 is the least positive

O(N)
"""
from typing import List

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        N=len(hours)
        C = [0] * (N+1)
        max_interval = 0
        seen = {}
        for i in range(1,N+1):
            C[i] = C[i-1] + (1 if hours[i-1] > 8 else -1)
            # it's already positive, interval can start from the beginning
            if C[i] > 0:
                max_interval = max(i, max_interval)
            # positive means we need subarray sum >= 1
            elif C[i]-1 in seen:
                max_interval = max(i - seen[C[i]-1], max_interval)
            
            # we want longest subarray, so store smallest index
            if C[i] not in seen:
                seen[C[i]] = i
        
        return max_interval

s = Solution()
print(s.longestWPI([9,9,6,0,6,6,9]))
print(s.longestWPI([9,9,9]))
        
        
        
