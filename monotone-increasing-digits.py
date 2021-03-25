"""
set 9 if it's not increasing
"""
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        res = []
        stack = []
        carry = 0
        for s in reversed(str(N)):
            if carry:
                s = str(int(s) - carry)
                carry = 0
            
            if stack and stack[-1] < s:
                for _ in range(len(stack)):
                    stack.pop()
                    res.append('9')
                
                if s == '0':
                    res.append('9')
                    carry = 1
                else:
                    stack.append(str(int(s) - 1))
            else:
                stack.append(s)
        
        if stack:
            res.extend(stack)
        
        return int(''.join(reversed(res)))

"""
simpler solution
if it's decreasing, decrease the previous num by 1 and mark the 9 digit index
"""
class Solution:
    def monotoneIncreasingDigits(self, num: int) -> int:
        A=list(str(num))
        N=len(A)
        
        j = N
        for i in reversed(range(1,N)):
            if A[i-1] > A[i]:
                A[i-1] = str(int(A[i-1]) - 1)
                j = i
        
        for j in range(j,N):
            A[j] = '9'
        
        return int(''.join(A))

s = Solution()
print(s.monotoneIncreasingDigits(332))
print(s.monotoneIncreasingDigits(1039))
print(s.monotoneIncreasingDigits(99049))
print(s.monotoneIncreasingDigits(214241))
print(s.monotoneIncreasingDigits(10))
print(s.monotoneIncreasingDigits(1234))
print(s.monotoneIncreasingDigits(14241))
print(s.monotoneIncreasingDigits(3245))
print(s.monotoneIncreasingDigits(11))
