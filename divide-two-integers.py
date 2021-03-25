"""
first find the leftmost bit of quotient, then fill the smaller digits of quotient one by one
100/8 = 12

100 = 0b1100100
8   =    0b1000

1 -> 2  -> 4  -> 8  -> 16 -> 12

8 -> 16 -> 32 -> 64 -> 128-> 96

1 -> 2 -> 4
3 -> 6 -> 12

O(32) = O(1)
"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if abs(dividend) < abs(divisor):
            return 0
        
        unsign = (dividend > 0) ^ (divisor > 0)
        
        dividend, divisor = abs(dividend), abs(divisor)
        
        ans = 1
        while divisor <= dividend:
            if divisor << 1 > dividend:
                break
            
            divisor <<= 1
            ans <<= 1
        
        cur = divisor >> 1
        cur_ans = ans >> 1
        
        while cur_ans > 0:
            if divisor + cur <= dividend:
                divisor += cur
                ans += cur_ans
            cur >>= 1
            cur_ans >>= 1
        
        ans = -ans if unsign else ans
        if -1<<31 <= ans < 1<<31:
            return ans
        return (1<<31)-1
            
        
s = Solution()
# print(s.divide(10,3))
# print(s.divide(7,-3))
# print(s.divide(0,1))
# print(s.divide(100,8))
# print(s.divide(99,4))
print(s.divide(-2147483648,-1))
print(s.divide(-2147483648,1))
