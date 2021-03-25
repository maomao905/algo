"""
1. prefix sum O(n)
2. compute all subarray sum O(n^2)
3. sort O(n^2log(n^2))
4. sum between left and right O(n^2)

O(n^2log(n^2))
"""
from typing import List
from itertools import *
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        N=len(nums)
        C = [0] + list(accumulate(nums))
        
        sub_sum = []
        
        for i in range(N):
            for j in range(i,N):
                sub_sum.append(C[j+1] - C[i])
        
        sub_sum.sort()
        return sum(sub_sum[left-1:right])%MOD

s = Solution()
print(s.rangeSum([1,2,3,4],4,1,5))
print(s.rangeSum([1,2,3,4],4,3,4))
print(s.rangeSum([1,2,3,4],4,1,10))
