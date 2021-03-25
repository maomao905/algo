"""
stack
final stack is the answer

1. keep the top of the stack is minimum
2. make sure it has enough element later than current element (satify k)

O(N)
"""

from typing import List

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        N=len(nums)
        for i in range(N):
            while stack and nums[i] < stack[-1] and k < N-i:
                stack.pop()
                k += 1
            
            if k > 0:
                stack.append(nums[i])
                k -= 1
        return stack

s = Solution()
print(s.mostCompetitive([3,5,2,6], 2))
print(s.mostCompetitive([2,4,3,3,5,4,9,6], 4))
print(s.mostCompetitive([2,1], 1))
print(s.mostCompetitive([71,18,52,29,55,73,24,42,66,8,80,2],3))
