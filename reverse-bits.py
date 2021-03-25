"""
00000010100101000001111010011100 (43261596)
00111001011110000010100101000000 (964176192)

- get the right-most bit n & 1
- shift the position using >> operator to move left of original bit
- add result and shift the position of reversed bit using << operator

time: O(32) = O(1)
space: O(1)
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        r = 0
        power = 31
        while n > 0:
            right_most_num = n & 1
            n >>= 1
            right_most_num <<= power
            r += right_most_num
            power -= 1
        return r
            
s = Solution()
print(s.reverseBits(43261596))
