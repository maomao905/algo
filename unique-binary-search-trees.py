"""
DP

if root node is fixed, then we know the range of left subtree and right subtree
n = 20
    10
   /  \
 1-9  11-20

11-20 means the same as 1-10
time: 2 + 3 + 4 + ... + n = O(N^2)
N=4, 4times iteration, N=3 3times iteration, we dont' have memo until it gets to zero
space: O(N)
"""

class Solution:
    def numTrees(self, n: int, memo={}) -> int:
        if n <= 1:
            return 1
        if n in memo:
            return memo[n]
        
        cnt = 0
        # i is root
        for i in range(1, n+1):
            # left * right
            cnt += self.numTrees(i-1, memo) * self.numTrees(n-i, memo)
        
        memo[n] = cnt
        return cnt

s = Solution()
print(s.numTrees(10))
        
        
