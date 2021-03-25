"""
16 = 10000
if num of bit1 is 1, it's power of two
we check every bit and count the 1
"""
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        cnt = 0
        while n > 0:
            right_most = n & 1
            if right_most == 1:
                cnt += 1
            
            n >>= 1
        
        return cnt == 1

"""
6 is not power of 2
6 = 0b00000110
-6 = reverse(0b00000110) + 0b00000001
   = 0b11111001 + 0b00000001
   = 0b11111010
6 & -6 = 0b00000110 & 0b11111010
       = 0b00000010 <--- this is not equal to 6

8 is power of 2
8 = 0b00001000
-8 = reverse(0b00001000) + 0b00000001
   = 0b11110111 + 0b00000001
   = 0b11111000
8&8 = 0b00001000 & 0b11111000
    = 0b00001000 <--- this is equal to 8

power of 2 means 1 appear only once in bits
-> seems taking & works because only 1 remains after taking &
-> how about taking 2's complement
-> when we take 2's complement of power of 2, we have 1-bit in the head and 0-bit in the back and only middle is the same 1
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return n == (n & -n)

"""
power of 2 - 1 is all the bits become 1 after the 1 bit of power of 2
8 = 0b00001000
8-1 = 0b00000111
8 & 7 = 0b000000000 = 0 <-- it must be 0 when you take x & (x-1) if x is power of 2

6 = 0b00000110
6-1 = 0b00000101
6 & 5 = 0b00000100 != 0
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return (n & n-1) == 0

s = Solution()
print(s.isPowerOfTwo(7))
print(s.isPowerOfTwo(8))
print(s.isPowerOfTwo(0))
