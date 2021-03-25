"""
(TLE)
brute-force
check difference any (i, j)
keep and update minimum and maximum value
O(N^2)
"""

from typing import List
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        N=len(nums)
        max_len = 1
        for i in range(N):
            min_val = max_val = nums[i]
            for j in range(i+1, N):
                min_val = min(min_val, nums[j])
                max_val = max(max_val, nums[j])
                if max_val - min_val > limit:
                    break
                
                max_len = max(max_len, j-i+1)
        return max_len

from collections import deque
"""
sliding window with two pointers
if diff <= limit, expand the window otherwise shrink the window

to get absolute difference within the window, we need to keep minimum and maximum value
min_q monotonically increasing queue and top element is minimum
max_q monotonically decreasing queue and top element is maximum

it's also possible to use heap but it takes O(NlogN)

time: O(N) space: O(N)
"""
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        N=len(nums)
        l = r = 0
        max_len = 0
        min_q = deque([0])
        max_q = deque([0])
        
        while r < N:
            # print(min_q, max_q, l, r)
            if nums[max_q[0]] - nums[min_q[0]] <= limit:
                max_len = max(max_len, r-l+1)
                r += 1
                if N <= r:
                    return max_len
                while min_q and (nums[r] < nums[min_q[-1]]):
                    min_q.pop()
                while max_q and (nums[r] > nums[max_q[-1]]):
                    max_q.pop()
                
                min_q.append(r)
                max_q.append(r)
            else:
                l += 1
                while min_q and min_q[0] < l:
                    min_q.popleft()
                    
                while max_q and max_q[0] < l:
                    max_q.popleft()
            
            
        return max_len

s = Solution()
# print(s.longestSubarray([8,2,4,7], 4))
print(s.longestSubarray([10,1,2,4,7,2], 5))
# print(s.longestSubarray([4,2,2,2,4,4,2], 0))
# print(s.longestSubarray([4,2,2,2,3,4,3,4,2], 1))
# print(s.longestSubarray([7,40,10,10,40,39,96,21,54,73,33,17,2,72,5,76,28,73,59,22,100,91,80,66,5,49,26,45,13,27,74,87,56,76,25,64,14,86,50,38,65,64,3,42,79,52,37,3,21,26,42,73,18,44,55,28,35,87],
# 63))
