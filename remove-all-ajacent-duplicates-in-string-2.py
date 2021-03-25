"""
stack

O(N) space O(N)
"""

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        N=len(s)
        for i in range(N):
            # found contiguous k letters
            if stack and stack[-1][0] == s[i] and stack[-1][1] + 1 == k:
                for _ in range(k-1):
                    stack.pop()
            else:
                j = stack[-1][1] + 1 if stack and stack[-1][0] == s[i] else 1
                stack.append((s[i], j))
        return ''.join([el[0] for el in stack])
                
s = Solution()
print(s.removeDuplicates('abcd', 2))
print(s.removeDuplicates('deeedbbcccbdaa', 3))
print(s.removeDuplicates('pbbcggttciiippooaais', 2))
