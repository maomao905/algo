"""
f(0) = f(1) = 0
f(k) = max(f(k-2)+K, f(k-1))

since circular array, we use two different start points
time: O(N), space: O(1)
"""
from typing import List
class Solution:
    
    def rob_from_first(self, nums):
        k_2 = 0
        k_1 = 0
        max_amount = 0
        for i in range(len(nums)-1):
            max_amount = max(k_2 + nums[i], k_1)
            k_2 = k_1
            k_1 = max_amount
        return max_amount
    
    def rob_from_second(self, nums):
        k_2 = 0
        k_1 = 0
        max_amount = 0
        for i in range(1, len(nums)):
            max_amount = max(k_2 + nums[i], k_1)
            k_2 = k_1
            k_1 = max_amount
        return max_amount
        
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_from_first(nums), self.rob_from_second(nums))

s = Solution()
print(s.rob([2,3,2]))
print(s.rob([1,2,3,1]))
print(s.rob([1]))
print(s.rob([1,2]))
            
