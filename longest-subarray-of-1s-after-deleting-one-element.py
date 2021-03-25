"""
prefix sum + suffix sum

O(N)
"""
from typing import List
from itertools import accumulate

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N=len(nums)
        prefix = list(accumulate(nums))
        prefix = [0] * N
        for i in range(N):
            if nums[i] == 0:
                continue
            if i - 1 >= 0:
                prefix[i] += prefix[i-1] + nums[i]
            else:
                prefix[i] = nums[i]
        
        suffix = [0] * N
        for i in reversed(range(N)):
            if nums[i] == 0:
                continue
            if i + 1 < N:
                suffix[i] += suffix[i+1] + nums[i]
            else:
                suffix[i] = nums[i]
        
        ans = 0
        for i in range(N):
            _sum = 0
            if i-1 >= 0:
                _sum += prefix[i-1]
            if i+1 < N:
                _sum += suffix[i+1]
            
            ans = max(_sum, ans)
        return ans

"""
DP

time O(N) space O(N)
"""
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N=len(nums)
        delete = [0] * N
        no_delete = [0] * N
        no_delete[0] = nums[0]
        for i in range(1,N):
            if nums[i] == 1:
                delete[i] = delete[i-1] + 1
                no_delete[i] = no_delete[i-1] + 1
            else:
                delete[i] = no_delete[i-1]
                no_delete[i] = 0
        return max(delete)

"""
sliding window
when we have only one zero in the window, it's ok, move on
once we have second zeros in the window, we have to shrink the window until num of zero becomes 1

time O(N) space O(1)
"""                
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N=len(nums)
        l = r = 0
        zero_cnt = 0
        ans = 0
        while r < N:
            if nums[r] == 0:
                zero_cnt += 1
            
            while zero_cnt > 1:
                if nums[l] == 0:
                    zero_cnt -= 1
                l += 1
            
            ans = max(ans, r-l+1-zero_cnt)
            r += 1
# 
        return min(ans, N-1)


s = Solution()
print(s.longestSubarray([1,1,0,1]))
print(s.longestSubarray([0,1,1,1,0,1,1,0,1]))
print(s.longestSubarray([1,1,1]))
print(s.longestSubarray([1,1,0,0,1,1,1,0,1]))
print(s.longestSubarray([0,0,0]))
