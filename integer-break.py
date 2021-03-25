"""
2 = 1+1 1*1=1
3 = 1+2 1*2=2
4 = 2+2 2*2=4
5 = 3+2 6
6 = 2+2+2 8
    3+3 9
7 = 2+2+2+1 8
    2+2+3   12
    4+3     12
    3+3+1   9
    2+5     10
8 = 2+2+2+2 16
    2+3+3   18
9 = 3+3+3   27
    2+7     14
    2+3+4   24
    4+5     20
    3+6     18
10 = 2+2+2+2+2 32
     2+2+3+3 36
     5 + 5 25

DP
time O(N^2) space O(N)
"""

class Solution:
    def integerBreak(self, n: int) -> int:
        def helper(k):
            if k in (1,2):
                return 1
            
            if k not in memo:
                memo[k] = max(max(helper(i), i) * max(helper(k-i), k-i) for i in range(1, (k//2)+1))
            return memo[k]
        
        memo = {}
        return helper(n)

"""
math

n = 2 + (n-2)

2 * (n-2) = 2n-4 >= n equals n >= 4
if n >= 4, we should divide

3*3 > 2*2*2

5 -> 2 + 3, 6 -> 3 + 3, 7 -> 3 + 3 + 1

we should choose 3 as much as we can

time O(N) space O(1)
"""

class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        elif n == 3:
            return 2
        
        remain = n % 3
        if remain == 1:
            remain = 4
            n -= 4
            
        return (3 ** (n//3)) * max(remain, 1)

s = Solution()
print(s.integerBreak(58))
print(s.integerBreak(4))
print(s.integerBreak(5))
print(s.integerBreak(10))
        
