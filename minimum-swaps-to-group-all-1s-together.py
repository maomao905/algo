"""
sliding window
keep sliding window whose size is 1's count
the answer is minimum number of 0's in the window

time O(N) space O(1)
"""
from typing import List

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        window_size = data.count(1)
        cur_zeros = min_zeros = data[:window_size].count(0)
        N=len(data)
        l = 0
        for r in range(window_size, N):
            cur_zeros -= data[l] == 0
            cur_zeros += data[r] == 0
            min_zeros = min(min_zeros, cur_zeros)
            l += 1
        return min_zeros

s = Solution()
print(s.minSwaps([1,0,1,0,1]))
print(s.minSwaps([0,0,0,1,0]))
print(s.minSwaps([1,0,1,0,1,0,0,1,1,0,1]))
print(s.minSwaps([1,0,1,0,1,0,1,1,1,0,1,0,0,1,1,1,0,0,1,1,1,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1]))
            
            
            
        
