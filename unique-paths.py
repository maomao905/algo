"""
recursive without memorization
first row and first column -> only one path
それ以外は左と上の行の合計になる
time: O(MN)
space: O(max(M,N))
"""
# class Solution(object):
#     def uniquePaths(self, m, n):
#         """
#         :type m: int
#         :type n: int
#         :rtype: int
#         """
#         if m == 1 or n == 1:
#             return 1
# 
#         return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1) 
"""
dynamic programming
time: O(MN)
space: O(MN)
"""
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1] * n for _ in range(m)]

        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row-1][col]+dp[row][col-1]

        return dp[m-1][n-1]

"""
math
"""
from math import factorial
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return factorial(m+n-2)//(factorial(m-1)*factorial(n-1))


s = Solution()
print(s.uniquePaths(3,7))
print(s.uniquePaths(3,2))
