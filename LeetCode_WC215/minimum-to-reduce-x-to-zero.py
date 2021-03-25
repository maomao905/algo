"""
[3,2,20,1,1,3], x = 10
<-x-><y><--x->
 
 y = total sum - x
 find the minimum window which sum is y

sliding window

time O(N) space O(1)
"""
from typing import List
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        N = len(nums)
        target = sum(nums) - x
        if target == 0:
            return N

        l = 0
        cur = 0
        ans = float('inf')
        for r in range(N):
            cur += nums[r]
            while l < r and cur > target:
                cur -= nums[l]
                l += 1
            
            if cur == target:
                ans = min(ans, N-(r-l+1))
        
        return -1 if ans == float('inf') else ans
            
            
        

s = Solution()
print(s.minOperations([4,3,2,3,5,1,7], 14))
print(s.minOperations([1,1,4,2,3], 5))
print(s.minOperations([5,6,7,8,9], 4))
print(s.minOperations([1,1,1], 3))
            
        
