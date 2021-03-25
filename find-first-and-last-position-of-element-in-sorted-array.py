"""
[5,6,6,7,7,8,8,10] target = 8
two binary search for left and right boundary

binary search for left boundary
l  r  mid
0  7  3   nums[3] = 7 <-- round off
4  7  5   nums[5] = 8
4  5  4   nums[4] = 7 <-- if mid is target, mid position becomes right
5  5      left == right -> nums[5] is the left boundary

binary search for right boundary
l  r  mid
0  7  4   nums[4] = 7 <-- round up
4  7  6   nums[6] = 8 <-- if mid is target, mid position becomes left
6  7  7   nums[7] = 10
6  6      left == right -> nums[6] is the right boundary

no target case (target = 9)
binary search for left boundary
l  r  mid
0  7  3   nums[3] = 7 <-- round off
4  7  5   nums[5] = 8
6  7  6   nums[6] = 8
7  7  7   nums[7] = 10 <-- left == right but nums[7] != target, which means target is not found

binary search for right boundary
l  r  mid
0  7  4   nums[4] = 7 <-- round up
4  7  6   nums[6] = 8 <-- if mid is target, mid position becomes left
7  7  7   nums[7] = 10 <-- left == right but nums[7] != target, which means target is not found

time: O(logN)
space: O(1)
"""
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search_for_left_boundary():
            left, right = 0, len(nums) - 1
            
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    right = mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return left

        def binary_search_for_right_boundary(start):
            left, right = start, len(nums) - 1
            
            while left < right:
                diff = right - left
                mid = left + (diff // 2) + diff % 2
                if nums[mid] == target:
                    left = mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return left
        
        if len(nums) == 0:
            return [-1, -1]
        
        left = binary_search_for_left_boundary()
        
        # target is not found
        if nums[left] != target:
            return [-1, -1]
        
        right = binary_search_for_right_boundary(left)
        
        return [left, right]

s = Solution()
print(s.searchRange(nums = [5,7,7,8,8,10], target = 8))
print(s.searchRange(nums = [5,7,7,8,8,10], target = 6))
print(s.searchRange(nums = [], target = 0))
