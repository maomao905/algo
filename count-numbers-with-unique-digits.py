class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        elif n == 1:
            return 10

        dp = [0] * n
        dp[0], dp[1] = 10, 9*9
        choices = 8
        for i in range(2,n):
            dp[i] = dp[i-1] * choices
            choices -= 1
        return sum(dp)
