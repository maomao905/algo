"""
time O(N) space O(N)
"""
from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        hs = set(arr)
        N=len(arr)
        
        n = 0
        for _ in range(k):
            if n+1 in hs:
                n += 1
                while n in hs:
                    n += 1
            else:
                n += 1
        return n

"""
binary search

[2,3,4,7,11]
arr[i] - i + 1
2-(0+1) = 1 is missing
3-(1+1) = 1 is missing
4-(2+1) = 1 is missing
7-(3+1) = 3 is missing
11-(4+1) = 6 is missing

binary search to find the exact index (k is missing)

if k == 1 in above example,
we need to find the leftmost index of '1 is missing', then arr[i]-1 is the answer
if k == 5 in above example,
after binary search, arr[pivot] == 11 and 6 is missing
11 - (6 - 5) - 1 = 9 is the answer

time O(logN) space O(1)
"""

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        N=len(arr)
        l,r=0,N-1
        
        while l <= r:
            mid = l + (r-l)//2
            missing = arr[mid] - (mid+1)
            if missing >= k:
                r = mid-1
            else:
                l = mid+1

        return l + k
            

s = Solution()
print(s.findKthPositive([2,3,4,7,11],5))
# print(s.findKthPositive([1,2,3,4],2))
# print(s.findKthPositive([10],1))
# print(s.findKthPositive([1,1,1,1],1))
print(s.findKthPositive([1,2],1))
# 
