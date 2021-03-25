"""
find the smallest subarray to remove
nums = [6,3,5,2] p = 9
sum(nums) % p = 7
if we remove 7, the sum becomes divisible by p
-> find the subarray that sum's mod equals 7

nums mod cumulative sum
[6,0,5,7] 7 - x in hash map


[1,6,3,2] p = 9
[1,7,1,3] target = 3
"""
from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        N=len(nums)
        # mod cumulative sum
        for i in range(N):
            if i == 0:
                nums[i] %= p
            else:
                nums[i] = (nums[i] + nums[i-1]) % p
            
        target = nums[-1]
        # already divisible
        if target == 0:
            return 0
        
        seen = {0: 0}
        min_len = N
        # find the subarray that sum's mod equals target
        for i in range(N):
            diff = nums[i] - target
            if diff < 0:
                diff = p + diff
            
            if diff in seen:
                min_len = min(min_len, i - seen[diff] + 1)
            seen[nums[i]] = i+1
        return -1 if min_len == N else min_len

s = Solution()
print(s.minSubarray([3,1,4,2], 6))
print(s.minSubarray([6,3,5,2], 9))
print(s.minSubarray([1,2,3], 3))
print(s.minSubarray([1,2,3], 7))
print(s.minSubarray(nums = [1000000000,1000000000,1000000000], p = 3))
