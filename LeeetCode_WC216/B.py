"""
n: length
k: sum of ord
"""
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
print(s.getSmallestString(5, 73))
print(s.getSmallestString(1000, 1000))
            
