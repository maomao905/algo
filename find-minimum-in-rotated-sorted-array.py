"""
binary search
compare start <--> pivot/pivot <--> end
if start < pivot: ok, otherwise, there is a pivot inside, so binary search within that range
if pivot < pivot: ok, otherwise, there is a pivot inside

time: O(logN)
space: O(1)
"""
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        
        if nums[left] < nums[right]:
            return nums[0]
        
        while left < right:
            # print(left,right)
            mid = (left+right)//2
            # midよりも右側にかならずpivotがある
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                # x // 2は切り捨てなので、right = midにすると、勝手にrightが一つ左にずれてくれるイメージ
                right = mid
        
        return nums[left]

s = Solution()
print(s.findMin([3,4,5,1,2]))
print(s.findMin([3,4,5,6,1,2]))
print(s.findMin([4,5,6,7,0,1,2]))
print(s.findMin([1]))
print(s.findMin([1,2]))
print(s.findMin([1,2,3]))
