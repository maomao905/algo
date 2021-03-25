"""
non-decreasing subarray starting from the left
non-decreasing subarray ending at the right
minimize the middle length to make array non-decreasing (two pointers)

two pointers
1  2  3  10  0  7  8  9
<---ok---->  <---ok--->  
             <-------->  4 removed
<>              <----->  4 removed
<->             <----->  3 removed
<---->          <----->  2 removed = answer
<--------->              4 removed

time O(N) space O(N)
"""
from typing import List

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        N=len(arr)
        
        # non-decreasing subarray starting from the left
        left_end = 0
        for i in range(1,N):
            if arr[left_end] > arr[i]:
                break
            left_end = i
        
        if left_end == N-1:
            return 0
        
        # non-decreasing subarray ending at the right
        right_start = N-1
        for i in reversed(range(N-1)):
            if arr[right_start] < arr[i]:
                break
            right_start = i
        
        r = right_start
        ans = r
        
        for l in range(left_end+1):
            while r < N and arr[r] < arr[l]:
                r += 1
            ans = min(ans, r-l-1)
        
        return ans

s = Solution()
print(s.findLengthOfShortestSubarray([1,2,3,10,4,2,3,5]))
print(s.findLengthOfShortestSubarray([5,4,3,2,1]))
print(s.findLengthOfShortestSubarray([1,2,3]))
print(s.findLengthOfShortestSubarray([1]))
print(s.findLengthOfShortestSubarray([1,2,3,10,0,7,8,9]))
print(s.findLengthOfShortestSubarray([16,10,0,3,22,1,14,7,1,12,15]))
        
