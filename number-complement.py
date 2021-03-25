class Solution:
    def findComplement(self, num: int) -> int:
        ans = 0
        n = 0
        while num:
            ans |= (1 ^ (num & 1)) << n
            num >>= 1
            n += 1
        return ans

s = Solution()
print(s.findComplement(5))
print(s.findComplement(1))
print(s.findComplement(2))
