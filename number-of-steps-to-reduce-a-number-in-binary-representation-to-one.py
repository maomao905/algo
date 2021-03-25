class Solution:
    def numSteps(self, s: str) -> int:
        ans = 0
        n = int(s, 2)
        while n > 1:
            # if odd, + 2
            if n & 1:
                n += 1
                ans += 2
            else:
                ans += 1
            n >>= 1
            # if even, + 1
        return ans
        

s = Solution()
print(s.numSteps('1101'))
print(s.numSteps('10'))
print(s.numSteps('1'))
print(s.numSteps('11'))
