from itertools import zip_longest
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0
        for x, y in zip_longest(a[::-1], b[::-1]):
            x = int(x) if x else 0
            y = int(y) if y else 0
            
            s = x + y + carry
            if s >= 2:
                carry = 1
            else:
                carry = 0
            mod = s%2
            res.append(str(mod))
        
        if carry:
            res.append(str(carry))
        
        return ''.join(res[::-1])

s = Solution()
print(s.addBinary('1010', '1011'))
print(s.addBinary('11', '1'))
