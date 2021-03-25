"""
12431
1. find the greater element than current element in stack
stack [1,3,4] cur=2
2. find the smallest element than current element
pop [2]
ans = remaining digits + [3] + [1,2] + [4] = 13124

start from the right, store number in stack and once greater element is found, swap

O(log10(n))
"""

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = list(str(n))
        stack = []
        for i in reversed(range(len(s))):
            # check if there is a greater element in stack than current element
            if stack and stack[-1] > s[i]:
                # find the next greater element in stack than current element
                j = 0
                while stack[j] <= s[i]:
                    j += 1
                # swap current element with next greater element in stack
                s[i], stack[j] = stack[j], s[i]
                s[i+1:] = stack
                res = int(''.join(s))
                return res if res < 1<<31 else -1
            
            stack.append(s[i])
        
        return -1

s = Solution()
# print(s.nextGreaterElement(12))
print(s.nextGreaterElement(12432))
print(s.nextGreaterElement(12431))
                           # 12223344
print(s.nextGreaterElement(12443322))
