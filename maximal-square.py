"""
DP

x z
y a

dp[a] = min(dp[x], dp[y], dp[z]) + 1

time: O(MN)
space: O(MN)
"""

from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [len(matrix[0]) * [0] for _ in range(len(matrix))]
        
        max_area = 0
        for row in range(len(dp)):
            dp[row][0] = int(matrix[row][0])
            max_area = max(dp[row][0], max_area)
        
        for col in range(len(dp[0])):
            dp[0][col] = int(matrix[0][col])
            max_area = max(dp[0][col], max_area)
        
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][col] == '1':
                    dp[row][col] = min(dp[row-1][col-1], dp[row-1][col], dp[row][col-1]) + 1
                    max_area = max(dp[row][col], max_area)
        
        return max_area ** 2

s = Solution()
print(s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
print(s.maximalSquare([["0","1"],["1","0"]]))
print(s.maximalSquare([["1"]]))
