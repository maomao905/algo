"""
   p
  / \
c1  c2 return max(p+c1, p+c2, p)  ans = max(p+c1, p+c2, p, p+c1+c2)

time O(N) space O(H)
"""

from lib.Tree import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        ans = float('-inf')
        def dfs(node):
            if node is None:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)
            
            nonlocal ans
            ans = max(ans, node.val + max(l, r, l+r, 0))
            return max(l, r, 0) + node.val
            
        dfs(root)
        return ans


s = Solution()        
print(s.maxPathSum(make([1,2,3])))
print(s.maxPathSum(make([2,-1,-2])))
print(s.maxPathSum(make([-10,9,20,None,None,15,7])))
print(s.maxPathSum(make([5,4,8,11,None,13,4,7,2,None,None,None,1])))
