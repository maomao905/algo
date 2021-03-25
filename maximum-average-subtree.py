# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        def dfs(node):
            nonlocal ans
            if node is None:
                return 0, 0
            
            l_sum, l_num = dfs(node.left)
            r_sum, r_num = dfs(node.right)
            
            _sum = l_sum + r_sum + node.val
            num = l_num + r_num + 1
            
            ans = max(ans, _sum/num)
            return _sum, num
        
        ans = 0
        dfs(root)
        return ans
