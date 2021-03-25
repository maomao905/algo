"""
1.order matters [1,2,3], it cannot pop 3 and then 1
2.it cannot pop element that is not pushed

-> simulate push and pop operations
"""
from typing import List
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        N=len(pushed)
        j = 0 # popped index
        for i in range(N):
            stack.append(pushed[i])
            while stack and j < N and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return not stack

s = Solution()
print(s.validateStackSequences([1,2,3,4,5], [4,5,3,2,1]))
print(s.validateStackSequences([1,2,3,4,5], [4,3,5,1,2]))
print(s.validateStackSequences([1], []))
print(s.validateStackSequences([1,0], [1,0]))
            
            
