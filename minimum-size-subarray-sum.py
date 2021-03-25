"""
sum = 7, [2,3,1,2,4,3]
two pointers
2,3,1
x 2,3,1,2 -> 3,1,2
x 3,1,2,4 -> 1,2,4
x 1,2,4,3 -> x 2,4,3 -> 4,3

time: O(n)
space: O(1)
"""
from typing import List
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        start = 0
        end = 0
        min_length = float('inf')
        tmp_sum = 0
        
        while end < len(nums):
            if tmp_sum + nums[end] < s:
                tmp_sum += nums[end]
                end += 1
            else:
                tmp_sum -= nums[start]
                min_length = min(min_length, end-start+1)
                start += 1
            # print(start, end, tmp_sum)
        if min_length == float('inf'):
            return 0
        
        return min_length

s = Solution()
# print(s.minSubArrayLen(7, [2,3,1,2,4,3]))
# print(s.minSubArrayLen(11, [1,2,3,4,5]))
print(s.minSubArrayLen(15, [1,2,3,4,5]))
