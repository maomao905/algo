# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        def dfs(node):
            if node is None:
                return 0, 0
            
            if not node.left and not node.right:
                return node.val, 1
            
            l_val, l_level = dfs(node.left)
            r_val, r_level = dfs(node.right)
            
            _sum = 0
            max_level = max(l_level, r_level)
            if l_level == max_level:
                _sum += l_val
            if r_level == max_level:
                _sum += r_val
            return _sum, max_level+1
        
        _sum, _ = dfs(root)
        return _sum
