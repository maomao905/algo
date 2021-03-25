from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        N=len(tokens)
        for i in range(N):
            char = tokens[i]
            if char in ('+','-','*','/'):
                a = stack.pop()
                b = stack.pop()
                c = 0
                if char == '+':
                    c = a + b
                elif char == '-':
                    c = b - a
                elif char == '*':
                    c = a * b
                elif char == '/':
                    c = int(b / a)
                    
                stack.append(c)
            else:
                stack.append(int(char))
        return stack[0]

s = Solution()
print(s.evalRPN(['2','1','+','3','*']))
print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
print(s.evalRPN(["4","-2","/","2","-3","-","-"]))
            
