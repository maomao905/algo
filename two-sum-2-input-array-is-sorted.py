"""
two pointers
first and last of the array

time: O(N)
space: O(1)
"""

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        
        while left < right:
            sum = nums[left] + nums[right]
            if sum == target:
                return [left+1, right+1]
            elif sum < target:
                left += 1
            else:
                right -= 1
        
        return []

s = Solution()
print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([2,3,4], 6))
print(s.twoSum([-1,0], -1))
