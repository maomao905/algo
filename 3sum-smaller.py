"""
one element is fixed and it will be two sum smaller problem (two sum < target - x)

[-2,0,1,3] remain = 2
2 sum < remain

two pointers O(N)
sort the array only once O(NlogN)
left <-----> right
if the sum is larger than target, right-1
if the sum is smaller than target, add count of (right-left)
left = -2, right = 3
left + right < remain -> -2 and (0,1,3)

O(N^2 + logN) -> O(N^2)
"""
from typing import List

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        N=len(nums)
        
        cnt = 0
        for i in range(N):
            remain = target - nums[i]
            
            l,r = i+1, N-1
            
            while l < r:
                if nums[l] + nums[r] < remain:
                    cnt += r-l
                    l += 1
                else:
                    r -= 1
        return cnt

s = Solution()
print(s.threeSumSmaller([-2,0,1,3], 2))
print(s.threeSumSmaller([], 0))
print(s.threeSumSmaller([0], 0))
                
