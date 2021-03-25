"""
we have two conditions
1. we need all distinct characters
    - every unique character appears at least once
    - compute last position where each character appears beforehand
        - if it is not last character, we can delete current character
2. smaller subsequence
    - place smaller character as early as it can
        - stack
            - if smaller character appear later, we want it to come early
                - pop greater characters

O(N)
"""

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        N=len(s)
        last = {}
        for i in range(N):
            last[s[i]] = i
        
        stack = []
        n = len(set(s))
        seen = set()
        for i in range(N):
            if s[i] in seen:
                continue
            
            while stack and stack[-1] > s[i] and i < last[stack[-1]]:
                seen.discard(stack.pop())
            
            stack.append(s[i])
            seen.add(s[i])
        
        return ''.join(stack)

s = Solution()
print(s.smallestSubsequence('bcabc'))
print(s.smallestSubsequence('cbacdcbc'))
