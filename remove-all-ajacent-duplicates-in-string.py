class Solution:
    def removeDuplicates(self, s: str) -> str:
        N=len(s)
        stack = []
        for i in range(N):
            stack.append(s[i])
            while len(stack) > 1 and stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
        return ''.join(stack)
