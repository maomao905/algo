"""
stack to find the correct position
traverse forward to find min
 2  [2]
 6  [2,6]
 4  [2,4]  pop 6 and push 4, save the min index of 6
 8
 10
 9
 15

traverse backward to find max

time: O(N)
space: O(N)
"""

from typing import List
class Solution:
    def find_min(self, nums):
        stack = []
        min_idx = len(nums)
        
        for i in range(len(nums)):
            while stack and stack[-1][1] > nums[i]:
                idx, _ = stack.pop()
                min_idx = min(idx, min_idx)
            stack.append((i, nums[i]))
        # print(min_idx)
        return min_idx
    
    def find_max(self, nums):
        stack = []
        max_idx = 0
        
        for i in reversed(range(len(nums))):
            while stack and stack[-1][1] < nums[i]:
                idx, _ = stack.pop()
                max_idx = max(idx, max_idx)
            stack.append((i, nums[i]))
        # print(max_idx)
        return max_idx
            
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        return max(self.find_max(nums) - self.find_min(nums) + 1, 0)

"""
keep min and max

if the array is sorted, 
    max_so_far <= nums[i]
    min_so_far >= nums[i] in reverse order

thus, if the above condition is not satisfied, mark the index as right and left
O(N)
O(1)
"""
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        N=len(nums)
        mi, mx = float('inf'), float('-inf')
        left, right = N, -1
        # find right
        for i in range(N):
            if mx > nums[i]:
                right = i
            mx = max(mx, nums[i])
        
        # find left
        for i in reversed(range(N)):
            if mi < nums[i]:
                left = i
            mi = min(mi, nums[i])
        
        return max(right - left + 1, 0)

s = Solution()
print(s.findUnsortedSubarray([2,6,4,8,10,9,15]))
print(s.findUnsortedSubarray([1,2,3,4]))
print(s.findUnsortedSubarray([1]))
