"""
- DFS (post-order traversal)
    - store the sum up to the current node in hash map
    - when DFS ends at root node, the sum of root node is the sum of entire tree
- check total sum / 2 matches in hash map
- time and space: O(N)

    5            30
   / \          /  \
  10 10   ->   10  15  
    /  \           / \
   2   3          2   3

30 / 2 = 15, which matches in hash map -> true
"""

from lib.Tree import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: TreeNode) -> bool:
        hs = set()
        def dfs(node):
            if node is None:
                return 0
            sum_left = dfs(node.left)
            sum_right = dfs(node.right)
            sum = sum_left + sum_right + node.val
            if node is not root:
                hs.add(sum)
            return sum
        
        total_sum = dfs(root)
        
        if total_sum % 2 == 1:
            return False
        target = total_sum // 2
        return target in hs

s = Solution()
print(s.checkEqualTree(make([5,10,10,None,None,2,3])))
print(s.checkEqualTree(make([1,2,10,None,None,2,20])))
print(s.checkEqualTree(make([0,-1,1])))
        
