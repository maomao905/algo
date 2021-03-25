"""
(WA)
"""
class Solution:
    def getSum(self, a: int, b: int) -> int:
        ans = 0
        carry = 0
        i = 0
        while i < 32 and a or b:
            temp = 0
            if a & 1 and b & 1:
                # 2 + 1 (carry) = 1 and carry 1
                # 2 + 0 (carry) = 0 and carry 1
                temp |= carry
                carry = 1
            elif a & 1 or b & 1:
                # 1 + 1 (carry) = 0 and carry 1
                # 1 + 0 (carry) = 1 and carry 0
                temp |= (1 ^ carry)
            else:
                # a == b == 0
                temp |= carry
                carry = 0
            ans |= (temp << i)
            # print(a & 1, b & 1, temp, bin(ans))
            a >>= 1
            b >>= 1
            i += 1
        
        if i < 32 and carry:
            ans |= (1 << i)
            
        return ans

"""
use a for addition without carry (xor)
use b for carry

it causes infinite loop in Python
"""
class Solution:
    def getSum(self, a: int, b: int) -> int:
        i = 0
        while b != 0 and i < 32:
            carry = a & b
            a ^= b
            b = carry << 1
            i += 1
        return a if i < 32 else 0
                

s = Solution()
# print(s.getSum(1,2))
# print(s.getSum(2,4))
print(s.getSum(5,10))
print(s.getSum(-3,-1))
print(s.getSum(-20,2))
print(s.getSum(-14,16))
print(s.getSum(-1,1))
