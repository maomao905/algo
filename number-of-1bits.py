"""
Hamming weight
n & n-1 -> we know the least significant 1 bit in n

8 & 7 = 0 because 8 = 1000, and least significant bit is removed, then all bits become zero

time: O(32) = O(1) if it's 32 bit integers
space: O(1)
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        
        while n != 0:
            n &= n-1
            cnt += 1
        return cnt

"""
check each bit and it's zero by ANDing 1 bit and continue by shifting
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        mask = 1
        
        for i in range(32):
            if (n&mask) != 0:
                bits += 1
            mask <<= 1
        
        return bits

s = Solution()
print(s.hammingWeight(1021))
