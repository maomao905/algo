"""
(TLE)
fix first 2 numbers, then check all other numbers are possible with remaining digits
O(N^2)
"""
from typing import List
class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        mx = 2**32-1
        max_size = len(str(mx))
        res = []
        # @profile
        def helper(i, comb):
            if i == N:
                return comb
            
            if i > N:
                return []
            
            if len(comb) >= 2:
                n = comb[-1] + comb[-2]
                # check if it's within 2^31-1
                if n > mx:
                    return []
                
                n_str = str(n)
                if S.startswith(n_str, i):
                    comb.append(n)
                    r = helper(i+len(n_str), comb)
                    if r:
                        return r
                    comb.pop()
                else:
                    return []
            
            r = []
            n = 0
            for j in range(i,min(N-1,i+max_size)):
                # ignore leading zero number
                if i != j and S[i] == '0':
                    break
                
                n *= 10
                n += int(S[j])
                
                comb.append(n)
                r = helper(j+1, comb)
                if r:
                    break
                
                comb.pop()
                
            return r
        
        N=len(S)
        return helper(0,[])

"""
O(N^2)
"""
class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        N=len(S)
        MAX = 2**31-1
        max_size = len(str(MAX))
        res = []
        
        for i in range(min(N-1,max_size)):
            # leading zero is invalid
            if i != 0 and S[0] == '0':
                break
            
            x = int(S[:i+1])
            y = 0
            for j in range(i+1,min(N-1,i+max_size)):
                # leading zero is invalid
                if i != j and S[i+1] == 0:
                    break
                
                y *= 10
                y += int(S[j])
                fib = [x, y]
                k = j+1
                while k < N:
                    z = fib[-1] + fib[-2]
                    if z > MAX:
                        break
                    str_z = str(z)
                    if not S.startswith(str_z, k):
                        break
                    
                    fib.append(z)
                    k += len(str_z)
                
                if k == N and len(fib) >= 3:
                    return fib
        return []
                    
s = Solution()
print(s.splitIntoFibonacci('123456579'))
print(s.splitIntoFibonacci('11235813'))
print(s.splitIntoFibonacci('112358130'))
print(s.splitIntoFibonacci('0123'))
print(s.splitIntoFibonacci('1101111'))
print(s.splitIntoFibonacci('1011'))
