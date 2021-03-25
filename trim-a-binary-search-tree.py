from lib.Tree import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def dfs(node):
            if node is None:
                return
                
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            
            if node.val < low:
                return node.right
            elif node.val > high:
                return node.left
            else:
                return node
        
        return dfs(root)

s = Solution()
print(show(s.trimBST(make([1,0,2]),1,2)))
print(show(s.trimBST(make([3,0,4,None,2,None,None,1]),1,3)))
print(show(s.trimBST(make([1]),1,2)))
print(show(s.trimBST(make([1,None,2]),1,3)))
print(show(s.trimBST(make([1,None,2]),2,4)))
