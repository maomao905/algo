"""
(TLE)
DP

O(N^2 * m)
"""

from typing import List
from itertools import accumulate
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def helper(i, k):
            if k == 0:
                return C[-1] - C[i]
            
            if (i,k) not in memo:
                memo[i,k] = min([max(helper(j+1, k-1), C[j+1] - C[i]) for j in range(i,N-k)])
            
            return memo[i,k]
        
        C = [0] + list(accumulate(nums))
        memo = {}
        N=len(nums)
        return helper(0, m-1)

"""
binary search

left = maximum value of the array
right = total sum of the array

cut the array in the way that sum is close to mid but less than mid
if the number of cuts <= m, mid is too big
if the number of cuts > m, mid is too small

O(Nlog(sum of the array))
"""
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        N=len(nums)
        def cuts(s):
            n = 1
            cur = 0
            for i in range(N):
                cur += nums[i]
                if cur > s:
                    n += 1
                    cur = nums[i]
                    if n > m:
                        return n
            return n
            
        l,r = max(nums), sum(nums)
        while l<r:
            mid = (l+r)//2
            if cuts(mid) <= m:
                r = mid
            else:
                l = mid+1
        return l
        
        
        
        
        
s = Solution()
print(s.splitArray([7,2,5,10,8],2))
print(s.splitArray([1,2,3,4,5],2))
print(s.splitArray([1,4,4],3))
