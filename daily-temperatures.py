"""
heap does not work

stack

[73,74,75,71,69,72,76,73]
-> look back because we don't know the future but know the past
73  [] -> 0
76  [73] -> 0 and pop 73 because 76 > stack[-1] -> [76]
72  [76,72] 72 is smaller than stack[-1] -> 1
69  [76,72,69] 69 is smaller than stack[-1] -> 1
71  [76,72,71] pop -> 2
75  [76,75] pop 2times -> 4 we need to store the index of stack items
74  [76,75,74] -> 1
73  [76,75,74,73] -> 1

time: O(N)
space: O(N)
"""

from typing import List
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0] * len(T)
        stack = []
        
        for i in reversed(range(len(T))):
            while len(stack) > 0 and T[i] >= stack[-1][0]:
                stack.pop()
            
            if len(stack) == 0:
                ans[i] = 0
            else:
                ans[i] = stack[-1][1] - i
            stack.append((T[i], i))
                
        return ans

s = Solution()
print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(s.dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))
