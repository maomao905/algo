"""
1. find the pivot first
2. find target is left or right to the pivot
3. binary search to find the target

time: O(logN) for 1 and O(logN) for 3 -> O(logN)
space: O(1)
"""

class Solution(object):
    def find_pivot(self, nums):
        left, right = 0, len(nums)-1

        while left < right:
            mid = (left + right) // 2
            # right側にpivot(最小値)があるかをcheck
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid

        return left

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pivot_index = self.find_pivot(nums)

        left, right = 0, len(nums)-1
        if nums[pivot_index] <= target <= nums[-1]:
            left = pivot_index
        else:
            right = pivot_index-1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        if nums[left] != target:
            return -1

        return left

"""
one-pass solution
always check if target is located in non-rotated array or not -> we can narrow down the scope correctly
"""
class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            # non-rotated array in left
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        if nums[left] != target:
            return -1
        return left

s = Solution()
print(s.search([4,5,6,7,0,1,2], 0))
print(s.search([4,5,6,7,0,1,2], 3))
print(s.search([1], 0))
        
        
