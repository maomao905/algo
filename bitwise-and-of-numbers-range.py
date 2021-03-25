"""
if we take AND with 2^n, we always get 2^n because only one digit is set

2^m & 2^n = 0

2^n & [2^(n-1), 2^n] = 2^n

if leftmost 1-bit is the same, we have to check right
leftmost 1-bit remains, and need to check right remaining bits until leftmost 1-bit is the same
"""

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        def get_leftmost_one_bit(i):
            for j in (1,2,4,8,16,32):
                i |= (i >> j)
            
            i += 1
            return i >> 1
        
        ans = 0
        while m > 0 and n > 0:
            _m = get_leftmost_one_bit(m)
            _n = get_leftmost_one_bit(n)
            # print('left', _m,_n)
            if _m != _n:
                return ans
            
            ans += _m
            m -= _m
            n -= _n
            # print(m,n)
        return ans

"""
find the common left 1-bit by shifting
[110101, 110001] -> 110000

if there is no common 1-bit, shifting all digits and it becomes 0 when n << cnt
[11000,101000]
"""
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        cnt = 0
        while m != n:
            m >>= 1
            n >>= 1
            cnt += 1
        
        return m << cnt
        
"""
unset right-most 1-bit when m < n
m: 101
n: 111 -> 110 -> 100

ans = m & n
"""
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while m < n:
            n &= n-1
        
        return m & n
        
s = Solution()
print(s.rangeBitwiseAnd(5,7))
print(s.rangeBitwiseAnd(0,1))
print(s.rangeBitwiseAnd(10,9))        
