# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        def dfs(node, is_first):
            if node is None:
                return False
            
            if is_first:
                seen.add(node.val)
            else:
                remain = target - node.val
                if remain in seen:
                    return True
            
            return dfs(node.left, is_first) or dfs(node.right, is_first)
        
        seen = set()
        dfs(root1, True)
        return dfs(root2, False)
