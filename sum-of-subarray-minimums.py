"""
how many subarrays does it have when the current element is minimum in the subarray

monotonic stack
given [3,1,2,4]
1. previous less element
[-1,-1,1,2] 
distance from previous less element
[1,2,1,1]
2. next less element
[1,-1,-1,-1]
distance from next less element
[1,3,2,1]

answer = 1*1*3 + 2*3*1 + 1*2*2 + 1*1*4 = 3+6+4+4 = 17

given [11,81,94,43,3]
1. previous less element
distance from previous less element
[1,1,1,3,5]
2. next less element
distance from next less element
[4,2,1,1,1]

answer = 1*4*11 + 1*2*81 + 1*1*94 + 3*1*43 + 5*1*3 = 444

O(N)
"""

from typing import List
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        N=len(arr)
        
        # previous less element
        prev_less_dist = [0] * N
        stack = []
        for i in range(N):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            d = i - stack[-1] if stack else i + 1
            prev_less_dist[i] = d
            stack.append(i)
        
        # next less element
        next_less_dist = [0] * N
        stack = []
        for i in reversed(range(N)):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            d = stack[-1] - i if stack else N-i
            next_less_dist[i] = d
            stack.append(i)
        
        return sum(arr[i] * prev_less_dist[i] * next_less_dist[i] for i in range(N)) % (10**9+7)
            
s = Solution()        
print(s.sumSubarrayMins([3,1,2,4]))
print(s.sumSubarrayMins([11,81,94,43,3]))
print(s.sumSubarrayMins([3,3,3]))
