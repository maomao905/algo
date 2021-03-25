"""
two sum
hashset
"""

from lib.Tree import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        seen = set()
        
        def dfs(node):
            if node is None:
                return False
            
            target = k - node.val
            if target in seen:
                return True
            
            seen.add(node.val)
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)
        
s = Solution()            
print(s.findTarget(make([5,3,6,2,4,None,7]),9))
print(s.findTarget(make([5,3,6,2,4,None,7]),28))
print(s.findTarget(make([2,1,3]),4))
        
