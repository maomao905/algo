class Solution:
    def calculate(self, s: str) -> int:
        parens = {} # start: end
        stack = []
        N=len(s)
        for i in range(N):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                parens[stack.pop()] = i
        
        def cal(i,j):
            stack = []
            op = '+'
            while i <= j:
                if s[i] == ' ':
                    i += 1
                    continue
                
                if s[i] in ('+', '-'):
                    op = s[i]
                    i += 1
                    continue
                
                n = 0
                if s[i] == '(':
                    n = cal(i+1, parens[i]-1)
                    i = parens[i] + 1
                # integer
                else:
                    start = i
                    while i <= j and s[i].isdigit():
                        i += 1
                    n = int(s[start:i])
                
                if op == '-':
                    n = -n
                    op = '+'
                
                stack.append(n)
            
            return sum(stack)
            
        return cal(0,N-1)

s = Solution()
print(s.calculate('1 + 1'))
print(s.calculate('2-1 + 2'))
print(s.calculate('(1+(4+5+2)-3)+(6+8)'))
print(s.calculate("2147483647"))
print(s.calculate("- (3 + (4 + 5))"))
print(s.calculate("1-11"))
print(s.calculate("1-(5)"))
        
                
            
