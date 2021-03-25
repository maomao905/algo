"""
calculate max day at each window k size
binary search to find the minimum days to make all bouquets

why we can use binary search?
if i days is enough to make bouquets, all j days is also enough to make bouquets where j > i
so, there's a monotonicity and binary search comes in

O(N + (N-k)log(N-k))
"""

from typing import List
from collections import deque

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        N=len(bloomDay)
        if N < k * m:
            return -1
        
        max_days = []
        q = deque()
        
        for i in range(N):
            while q and q[0] <= i-k:
                q.popleft()
            
            while q and bloomDay[q[-1]] < bloomDay[i]:
                q.pop()
            
            q.append(i)
            
            if i >= k-1:
                max_days.append(bloomDay[q[0]])
        
        def is_possible(day):
                cnt = 0
                i = 0
                while i <= N-k:
                    if max_days[i] <= day:
                        cnt += 1
                        if cnt == m:
                            return True
                        i += k
                    else:
                        i += 1
                return False
        
        l,r = min(bloomDay), max(bloomDay)
        while l < r:
            mid = l + (r-l)//2
            # it's possible to make all flowers with mid days, maybe we can reduce days
            if is_possible(mid):
                r = mid
            else:
                # we need more days to get all flowers
                l = mid+1
        return l
            
s = Solution()                
print(s.minDays([1,10,3,10,2],3,1))
print(s.minDays([1,10,3,10,2],3,2))
print(s.minDays([7,7,7,7,12,7,7], m = 2, k = 3))
print(s.minDays([1000000000,1000000000], m = 1, k = 1))
print(s.minDays([1,10,2,9,3,8,4,7,5,6], m = 4, k = 2))
print(s.minDays([30,49,11,66,54,22,2,57,35],3,3))
        
        
