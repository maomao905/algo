"""
stack

2[bc]
when we encounter ], we pop until [, and then pop to get count, if count is string, it's 1
"""

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for l in s:
            if l == ']':
                w = ''
                while stack[-1] != '[':
                    w = stack.pop() + w
                
                stack.pop()
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                w *= int(num)
                
                stack.append(w)
            else:
                stack.append(l)
        
        return ''.join(stack)

s = Solution()
print(s.decodeString('3[a]2[bc]'))
print(s.decodeString('3[a2[c]]'))
print(s.decodeString("2[abc]3[cd]ef"))
print(s.decodeString("abc3[cd]xyz"))
print(s.decodeString("10[leetcode]"))
print(s.decodeString("20[a10[bc]]"))
        
