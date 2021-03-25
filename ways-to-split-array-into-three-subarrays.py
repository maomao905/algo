"""
cumulative sum
[1,2,2,2,5,0] -> [1,3,5,7,12,12]

fix left binary search to find the range of mid, right is automatically determined
left [1] 2 <= mid sum <= (12-1)//2 + 1 = 6
               [3,5]
left [1,2] 6 <= mid sum <= (12-3)//2 + 3 = 7
                [7]

O(NlogN) space O(N)
"""

from typing import List
from itertools import accumulate
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        def binary_search_min(l, r, target):
            while l < r:
                mid = l + (r-l)//2
                if cum_sum[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            return l
        
        def binary_search_max(l, r, target):
            while l < r:
                mid = l + (r-l)//2
                if cum_sum[mid] <= target:
                    l = mid + 1
                else:
                    r = mid
            return l
        
        cum_sum = list(accumulate(nums))
        
        ans = 0
        N=len(nums)
        for i in range(N-2):
            mid_sum_min = cum_sum[i]*2
            mid_sum_max = (cum_sum[N-1]-cum_sum[i])//2 + cum_sum[i]
            if mid_sum_min > mid_sum_max:
                break
            
            min = binary_search_min(i+1, N-1, mid_sum_min)
            max = binary_search_max(min, N-1, mid_sum_max)
                
            ans += max-min
        
        return ans % (10**9+7)

"""
sliding window
<-left->j<-mid->k<-right->
if left is fixed, minimum mid j and maximum mid k is fixed and k-j+1 is the valid range when left is ith index
and j and k only move forward

time O(N) space O(N)
"""
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        MOD = 10**9+7
        cum_sum = list(accumulate(nums))
        ans = 0
        N=len(nums)
        j=k=0
        for i in range(N-2):
            mid_sum_min = cum_sum[i]*2
            mid_sum_max = (cum_sum[N-1]-cum_sum[i])//2 + cum_sum[i]
            
            j = max(i+1, j)
            while j < N and cum_sum[j] < mid_sum_min:
                j += 1
            
            while k < N-1 and cum_sum[k] <= mid_sum_max:
                k += 1
            
            if j > k:
                break
            else:
                ans += (k - j)%MOD
        return ans % MOD

s = Solution()
# print(s.waysToSplit([1,1,1]))
print(s.waysToSplit([1,2,2,2,5,0]))
# print(s.waysToSplit([3,2,1]))
# print(s.waysToSplit([0,3,3]))
            
        
