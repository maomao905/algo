"""
stack

O(N)
"""
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        N=len(s)
        stack = []
        remove = set()
        for i in range(N):
            c = s[i]
            if c == '(':
                stack.append(i)
            elif c == ')':
                if not stack:
                    remove.add(i)
                else:
                    stack.pop()
        
        remove.update(stack)
        
        res = []
        for i in range(N):
            if i not in remove:
                res.append(s[i])
        return ''.join(res)

s = Solution()
print(s.minRemoveToMakeValid('lee(t(c)o)de)'))
print(s.minRemoveToMakeValid('a)b(c)d'))
print(s.minRemoveToMakeValid('))(('))
print(s.minRemoveToMakeValid('(a(b(c)d)'))
                
