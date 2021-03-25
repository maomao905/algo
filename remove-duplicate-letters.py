"""
we need to output all chars
    if the char appears last, then we must use that if is's not used before
    if it's not the last char, then we can remove
lexicographical order
    place smallest char as early as it can

O(N)
"""

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {}
        N=len(s)
        for i in range(N):
            last[s[i]] = i
        
        stack = []
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
print(s.removeDuplicateLetters('bcabc'))
print(s.removeDuplicateLetters('cbacdcbc'))
