# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if node is None:
                return
            
            nonlocal s
            
            dfs(node.right)
            node.val += s
            s = node.val
            dfs(node.left)
        
        s = 0
        dfs(root)
        return root
