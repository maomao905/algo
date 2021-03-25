"""
if array contains 1-N, answer is N+1
if not, return the missing number

we can do this by using index
time O(N) space O(N)
"""
from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        
        hs = set(nums)
        N=len(nums)
        for i in range(N):
            if i+1 not in hs:
                return i+1
        return N+1

"""
swap
time O(N) space O(1)

[3,4,-1,1]
[-1,4,3,1]
[-1,1,3,4]
[1,-1,3,4]
"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N=len(nums)
        for i in range(N):
            while i+1 != nums[i] and 1 <= nums[i] <= N:
                temp = nums[i]
                if nums[i] == nums[temp-1]:
                    break
                nums[i], nums[temp-1] = nums[temp-1], nums[i]
        
        for i in range(N):
            if i+1 != nums[i]:
                return i+1
        return N+1

s = Solution()
print(s.firstMissingPositive([1,2,3]))
print(s.firstMissingPositive([1,2,0]))
print(s.firstMissingPositive([3,4,-1,1]))
print(s.firstMissingPositive([7,8,9,11,12]))
print(s.firstMissingPositive([1,1]))
print(s.firstMissingPositive([1,0,1]))
