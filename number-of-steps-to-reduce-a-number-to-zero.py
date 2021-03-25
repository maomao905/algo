class Solution:
    def numberOfSteps (self, num: int) -> int:
        ans = 0
        while num:
            # odd
            if num & 1:
                num &= num-1
            else:
                num >>= 1
            ans += 1
        return ans

class Solution:
    def numberOfSteps (self, n: int) -> int:
        ans = 0
        while n:
            ans += 2 if n & 1 else 1
            n >>= 1
        return max(ans - 1, 0)

s = Solution()
print(s.numberOfSteps(14))
print(s.numberOfSteps(8))
print(s.numberOfSteps(123))
                
