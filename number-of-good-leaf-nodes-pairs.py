# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
from lib.Tree import *
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(node):
            if node is None:
                d = [0] * N
                return d
            
            if not node.left and not node.right:
                d = [0] * N
                d[0] =  1
                return d
            ld = dfs(node.left)
            rd = dfs(node.right)
            # print(node.val, ld,rd)
            nonlocal ans
            for l in range(N):
                for r in range(N-l):
                    ans += ld[l] * rd[r]
            
            for i in reversed(range(N-1)):
                ld[i+1] = ld[i] + rd[i]
            ld[0] = 0
            return ld
        
        N=distance-1
        if N == 0:
            return 0
        ans = 0
        dfs(root)
        return ans

s = Solution()
print(s.countPairs(make([1,2,3,4,5,6,7]), 3))
print(s.countPairs(make([7,1,4,6,None,5,3,None,None,None,None,None,2]), 3))
