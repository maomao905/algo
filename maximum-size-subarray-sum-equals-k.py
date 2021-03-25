"""
subarray sum -> cumulative sum
how can I get maximum size

[1,-2,5,-2,3] k=3
[1,-1,4,2,5]
store cumulative sum and index in hash map
if there is a cumulative sum in hash map,
then we don't need to update the index because we want to find the maximum size
and always current index - smaller index leads to maximum size
and everytime we check there is cumulative sum - k in hash map
if it exists, we update maximum size

0: 1-3 = -2 no {0:0,1:1}
1: -1-3 = -4 no {0:0,1:1,-1:2}
2: 4-3 = 1 yes 2-1+1 = 2 {0:0,1:1,-1:2,4:3}
3: 2-3 = -1 yes 3-2+1=2 {0:0,1:1,-1:2,4:3,2:4}
4: 5-3 = 2 yes 4-4+1=1
-> maximum size is 2

time and space: O(N)
"""
from typing import List
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        cum_sum = {0: 0}
        prev = 0
        max_size = 0
        for i in range(len(nums)):
            n = nums[i]
            sum = prev + n
            _i = cum_sum.get(sum-k, -1)
            # print(cum_sum, sum)
            if _i != -1:
                max_size = max(i - _i + 1, max_size)
            
            if sum not in cum_sum:
                cum_sum[sum] = i+1
            prev = sum
        
        return max_size

s = Solution()
print(s.maxSubArrayLen([1,-1,5,-2,3], 3))
print(s.maxSubArrayLen([-2,-1,2,1], 1))
print(s.maxSubArrayLen([-1,1], 0))
        
        
        
        
        
