"""
k = 1
maximum subarray sum by Kadane's algorithm

k >= 2
case1:
<-- minus -><---- plus -------><-- minus -->
<----1th-------->          <-----nth----->
            <---><--------><-->
            suffix,(k-2)*sum,prefix

case2:
<-------------  k * sum ------------------>

time: O(N) space: O(1)
"""

from typing import List

class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        mod = 10**9 + 7
        max_sum = float('-inf')
        cur_sum = 0
        for x in arr:
            cur_sum += x
            if cur_sum < 0:
                cur_sum = 0
            max_sum = max(max_sum, cur_sum)
        
        if k == 1:
            return max(0, max_sum % mod)
        
        max_prefix_sum = float('-inf')
        prefix_sum = 0
        for x in arr:
            prefix_sum += x
            max_prefix_sum = max(max_prefix_sum, prefix_sum)
        
        whole_sum = prefix_sum
        
        max_suffix_sum = float('-inf')
        suffix_sum = 0
        for x in reversed(arr):
            suffix_sum += x
            max_suffix_sum = max(max_suffix_sum, suffix_sum)
        
        if whole_sum < 0:
            return max(0, max_sum, max_suffix_sum + max_prefix_sum) % mod
        else:
            return max(0, max_sum, max_suffix_sum + (k-2) * whole_sum + max_prefix_sum) % mod

s = Solution()
print(s.kConcatenationMaxSum([1,2], 3))
print(s.kConcatenationMaxSum([1,-2,1], 5))
print(s.kConcatenationMaxSum([-1,-2], 7))
print(s.kConcatenationMaxSum([-5,4,-4,-3,5,-3], 3))
print(s.kConcatenationMaxSum([2,-5,1,0,-2,-2,2], 2))
print(s.kConcatenationMaxSum([-9,13,4,-16,-12,-16,3,-7,5,-16,16,8,-1,-13,15,3], 6))
            
