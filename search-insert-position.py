from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        1 2 4 5 7
        x = 6
        pivot(4) <= x -> search from 4,5,7
        pivot(5) <= x -> search from 5,7
        pivot(7) <= x -> search from 5
        if search elements size == 1:
            if x == search element:
                return the position of search element
            else:
                if x < search element:
                    return the position of search element - 1
                else:
                    return the position of search element + 1
        time: O(logN)
        space: O(1)
        """
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            pivot = (left + right) >> 1
            if nums[pivot] == target:
                return pivot
            if nums[pivot] >= target:
                right = pivot-1
            else:
                left = pivot+1
        return left
        
s = Solution()
print(s.searchInsert([1,3,5,6], 5))
print(s.searchInsert([1,3,5,6], 2))
print(s.searchInsert([1,3,5,6], 7))
print(s.searchInsert([1,3,5,6], 0))
print(s.searchInsert([1], 0))
        
