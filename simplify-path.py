"""
stack

./ -> /
../ -> pop stack
... -> filename
// -> /
remove trailing slash

O(N)
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for s in path.split('/'):
            if not s or s == '.':
                continue
            
            if s == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(s)
        
        return '/' + '/'.join(stack)

s = Solution()
print(s.simplifyPath('/home/'))
print(s.simplifyPath('/../'))
print(s.simplifyPath('/home//foo/'))
print(s.simplifyPath('/a/./b/../../c/'))
print(s.simplifyPath('//'))
            
