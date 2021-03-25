"""
[10,5,2,6]

x DP
x cumulative product

reduce to sum subarray problem instead of product subarray problem

nums[i] * nums[j] * nums[k] = target
log(nums[i] * nums[j] * nums[k]) = log(target)
log(nums[i]) + log(nums[j]) + log(nums[k]) = log(target)

10 * 5 * 2 = 100
log(10) + log(5) + log(2) = log(100)

-> how to find the subarray which sum is less than log(target)
    -> cumulative sum
    -> cumulative sum is monotonically increasing
    -> binary search to find [i..j] in all elements

     10 5  2   6  k=17
sum  10 15 17 23 
     ---->        0 < 0 + k < 17  + 2
        -------> 23 < 10 + k      + 3
           ----> 23 < 17 + k      + 2
              -> 6 < k            + 1
O(NlogN)
"""

from typing import List
import math
from bisect import bisect_left
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        # take log
        N=len(nums)
        for i in range(N):
            nums[i] = math.log(nums[i])
        
        k = math.log(k)
        
        # calculate cumulative sum
        cum_sum = [0] * N
        for i in range(N):
            if i == 0:
                cum_sum[i] = nums[i]
            else:
                cum_sum[i] = cum_sum[i-1] + nums[i]
        
        ans = 0
        # binary search to find the sum range less than k
        for i in range(N):
            _k = cum_sum[i-1] + k if i > 0 else k
            j = bisect_left(cum_sum,_k)
            # this also works
            # find the right-most index which is greater than or equal to k
            # l, r = i, N
            # while l < r:
            #     mid = l + (r-l)//2 
            #     if cum_sum[mid] >= _k:
            #         r = mid
            #     else:
            #         l = mid + 1
            ans += j - i
        
        return ans

"""
sliding window (two pointers)
this solution is much simpler
expand if prod < k and if prod >= k moving the left pointer to right by one
O(N)
"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        N = len(nums)
        prod = 1
        left = 0
        cnt = 0
        for right in range(N):
            prod *= nums[right]
            while prod >= k:
                prod //= nums[left]
                left += 1

            cnt += right - left + 1

        return cnt

s = Solution()
print(s.numSubarrayProductLessThanK([10,5,2,6], 100))
# print(s.numSubarrayProductLessThanK([1,2,3], 0))
        
        
        
