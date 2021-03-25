"""
monotonic stack

stack keeps monotonically decreasing order
if we find greater element than stack[0], pop all from stack

to handle circular array,
we also need to keep last greater element

1. in first loop, find next greater element than stack[0]
   if found, pop everything and push current element
2. in second loop, find next greater element than stack[-1]
   if found, pop one element and continue

[1,2,1]

i j  stack
0 0  [1]
  1  2 > stack[0], pop everything [2]
  2  [2,1] end of the list
     go to second loop, find greater value than stack[-1]
  1 
  2  2 > stack[-1], pop [2]

time: O(N) space: O(N)
"""

from typing import List
from collections import deque

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        N=len(nums)
        max_stack = [] # monotonically decreasing
        min_stack = deque([]) # monotonically increasing
        res = [-1] * N
        
        for i in range(N):
            while max_stack and nums[max_stack[-1]] < nums[i]:
                j = max_stack.pop()
                res[j] = nums[i]
            
            max_stack.append(i)
            if not min_stack or (min_stack and nums[min_stack[-1]] < nums[i]):
                min_stack.append(i)
        
        # print(res)
        
        while True:
            while min_stack and nums[max_stack[-1]] >= nums[min_stack[0]]:
                min_stack.popleft()
            
            if not min_stack:
                break
            
            while max_stack and nums[max_stack[-1]] < nums[min_stack[0]]:
                j = max_stack.pop()
                res[j] = nums[min_stack[0]]
            
            if not max_stack:
                break
        
        return res

"""
simpler solution with same approach

two loops with monotonically decreasing stack (top of the stack is the maximum)
time and space: O(N)
"""
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        N=len(nums)
        stack = []
        res = [-1] * N
        for i in range(N*2):
            i %= N
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            stack.append(i)
        return res
        
s = Solution()
print(s.nextGreaterElements([1,2,1]))
print(s.nextGreaterElements([5,4,3,2,1]))
print(s.nextGreaterElements([1,2,3,4,5,6,5,4,5,1,2,3]))
