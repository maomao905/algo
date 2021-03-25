"""
1348621 -> 1361248
first digitからincreasingになっている限り、何もしない (8621)
decreasingになったら(4)、そのnumberが然るべきところにいくまでいったらswap(4 <--> 6)する(1368421)
increasingになっている部分をreverseする (1361248)

ref: https://www.nayuki.io/page/next-lexicographical-permutation-algorithm

time: O(N)
space: O(1)
"""
from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def get_first_decreasing_index():
            for i in reversed(range(1,N)):
                if nums[i] > nums[i-1]:
                    return i-1
            return -1
        
        def get_next_greater_index(i):
            for j in range(i+1, N):
                if nums[j] <= nums[i]:
                    return j-1
            return N-1
        
        N=len(nums)
        i = get_first_decreasing_index()
        if i == -1:
            nums.reverse()
            return
        
        j = get_next_greater_index(i)
        nums[i], nums[j] = nums[j], nums[i]
        # reverse
        nums[i+1:] = nums[-1:i:-1]

s = Solution()
nums = [1,3,4,8,6,2,1]
s.nextPermutation(nums); print(nums);
nums = [1,2,3]
s.nextPermutation(nums); print(nums);
nums = [1,1,5]
s.nextPermutation(nums); print(nums);
nums = [3,2,1]
s.nextPermutation(nums); print(nums);
nums = [1]
s.nextPermutation(nums); print(nums);
nums = [1,5,1]
s.nextPermutation(nums); print(nums);
