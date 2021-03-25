"""
swap next num if necessary

store previous num and greater/less flag

1 2 3 4 5
2 1
  1 3
    4 3
      3 5

time: O(N) space: O(1)
"""
from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        less = True
        for i in range(len(nums)-1):
            if less and nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
            elif not less and nums[i] < nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
            less = not less
        print(nums)        

s = Solution()
s.wiggleSort([3,5,2,1,6,4])
