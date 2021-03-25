"""
heap

1. sort to find the median O(nlogn)
2. calculate |arr[i] - ml| O(n)
3. heap to get k strongest values O(nlogk)

O(nlogn)
"""
from typing import List
from heapq import *
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        N=len(arr)
        
        median = sorted(arr)[(N-1)//2]
        
        return nlargest(k, arr, key=lambda x: (abs(x-median), x))

s = Solution()
print(s.getStrongest([1,2,3,4,5],2))
print(s.getStrongest([1,1,3,5,5],2))
print(s.getStrongest([6,-3,7,2,11],3))
print(s.getStrongest([-7,22,17,3],2))
