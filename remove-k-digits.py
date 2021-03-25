"""
- make smallest number
    - check from the beginning
    - if we meet smaller num, we should remove the larger num which appeared before
        - stack should be increasing
- avoid leading zero
    - zero will never be popped from stack because it's smallest
"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        N=len(num)
        if N == k:
            return '0'
        
        stack = []
        for n in num:
            while stack and k > 0 and stack[-1] > n:
                stack.pop()
                k -= 1
        
            stack.append(n)
        
        # pop remaining k digits
        stack = stack[:-k] if k else stack
        
        # remove leading zeros
        return ''.join(stack).lstrip('0') or '0'
        
s = Solution()
print(s.removeKdigits('1432219', 3))
print(s.removeKdigits('10200', 1))
print(s.removeKdigits('10', 2))
print(s.removeKdigits('11091501', 2))
print(s.removeKdigits('112', 1))
print(s.removeKdigits('11112', 2))
print(s.removeKdigits('1173', 2))
