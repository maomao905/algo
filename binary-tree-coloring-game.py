"""
optimal node for second player to choose is only 3 possible nodes
- parent node of x
    - n - (left subtree + right subtree + 1)
- left node of x
    - left subtree
- right node of x
    - right subtree

choose maximum node and check it goes over n/2 to win

O(N)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        ans = False
        def dfs(node):
            if node is None:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)
            
            if node.val == x:
                nonlocal ans
                ans = max(l,r,n-(l+r+1)) > n//2
            
            return l + r + 1
        
        dfs(root)
        return ans
