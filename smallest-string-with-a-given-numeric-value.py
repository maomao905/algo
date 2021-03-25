"""
n=3, k=27
27 - (3-0-1) * 26 <= 0 -> a
26 - (2-0-1) * 26 <= 0 -> a
25 - (1-0-1) * 26 > 0  -> y

O(N)      
"""

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = [0] * n
        for i in range(n):
            need = k - (n-i-1) * 26
            if need > 0:
                res[i] = chr(need + 96)
            else:
                res[i] = 'a'
            k -= max(need, 1)
        
        return ''.join(res)

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        if n == 0:
            return ''
        
        s = []
        while n > 0:
            v = (k - n + 1) 
            if v >= 26:
                s.append('z')
                n -= 1
                k -= 26
            else:
                s.append(chr(v + ord('a') - 1))
                n -= 1
                k -= v
        return ''.join(reversed(s))

s = Solution()
print(s.getSmallestString(3,27))
print(s.getSmallestString(5,73))
