"""
DFS pre-order
keep cumulative sum in hash map (counter)
at each node, we check the target sum exist
after reaching the leaf node, backtrack the hash map (decrement counter)

time: O(N)
space: O(N) in worst
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from library.tree import *

from collections import Counter
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        ans = 0
        cnt = Counter({0: 1})
        def dfs(node, cum_sum):
            nonlocal ans
            if node is None:
                return
            
            cum_sum += node.val
            target = cum_sum - sum
            if target in cnt:
                ans += cnt[target]
            
            cnt[cum_sum] += 1
            dfs(node.left, cum_sum)
            dfs(node.right, cum_sum)
            
            cnt[cum_sum] -= 1
        
        dfs(root, 0)
        return ans
            
s = Solution()
print(s.pathSum(make([10,5,-3,3,2,None,11,3,-2,None,1]), 8))
print(s.pathSum(make([5,4,8,11,None,13,4,7,2,None,None,5,1]),22))
