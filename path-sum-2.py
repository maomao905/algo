"""
DFS
pre-order traversal

we append the num from root to leaf and backtrack

time: traversal O(N), list copy O(N) -> O(N^2)
space: O(N) in worst
"""

from typing import List

from library.tree import TreeNode, make
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        res = []
        def dfs(node, nums):
            if node is None:
                return
            
            nums.append(node.val)
            if not node.left and not node.right and sum(nums) == target:
                res.append(list(nums))
                
            dfs(node.left, nums)
            dfs(node.right, nums)
            # backtrack
            nums.pop()
        
        dfs(root, [])
        return res

s = Solution()
print(s.pathSum(make([5,4,8,11,None,13,4,7,2,None,None,5,1]),22))
