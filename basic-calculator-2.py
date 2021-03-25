"""
stack

- +の場合は、stackに積むだけ
- *はすぐにmultiplyする (stack[-1] * current number)
- update number until we see operator and save it as num
- when we see another operator, num * stack[-1]
    - previous num (op) saved num (current op)
- 最後にstackに残ったものをすべて足したものが答えになる

time: O(N)
space: O(N)
"""

class Solution:
    def calculate(self, s: str) -> int:
        n = 0
        op = '+'
        stack = []
        N=len(s)
        
        for i in range(N):
            char = s[i]
            if char.isdigit():
                n = n * 10 + int(char)
            if char in '+-*/' or i == N-1:
                if op in '*/':
                    _n = stack.pop()
                    stack.append(_n * n if op == '*' else int(_n/n))
                elif op in '+-':
                    stack.append(n if op == '+' else -n)
                
                op = char
                n = 0
        
        return sum(stack)

s = Solution()
print(s.calculate('1*2 + 3'))
print(s.calculate('3/2'))
print(s.calculate('3 + 1*2'))
print(s.calculate('33 + 22'))
print(s.calculate('22   +    33 * 10'))
print(s.calculate("0-2147483647"))
print(s.calculate("1-1"))
print(s.calculate("14-3/2"))
