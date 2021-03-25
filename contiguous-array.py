"""
using hash map, we store the difference count between 0's and 1's and the current index
time: O(N)
"""

from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero_cnt, one_cnt = {}, {}
        zeros = ones = 0
        max_len = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            else:
                ones += 1
            
            if zeros == ones:
                max_len = i+1
            elif zeros > ones:
                diff = zeros - ones
                if diff in zero_cnt:
                    max_len = max(i - zero_cnt[diff], max_len)
                else:
                    zero_cnt[diff] = i
            else:
                diff = ones - zeros
                if diff in one_cnt:
                    max_len = max(i - one_cnt[diff], max_len)
                else:
                    one_cnt[diff] = i    
        return max_len    

s = Solution()
print(s.findMaxLength([0,1]))
print(s.findMaxLength([1,1,1,1,0,0]))
print(s.findMaxLength([0,1,1,0,1,1,1,0]))
print(s.findMaxLength([0,0,1,0,0,0,1,1]))
