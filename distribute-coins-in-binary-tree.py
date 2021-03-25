"""
DFS

get short coins and extra coins from child nodes
and reditribute them

the number of short coins at each node is the number of moves required to pass the coins from parent node
in the same way, the number of extra coins at each node is the number of moves required to pass the coins from parent node
at parent node, offset the short coins and extra coins - 1 (coin for current node), then pass the remaining to parent node

time O(N) space O(H)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from lib.Tree import *
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        def dfs(node):
            if node is None:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)
            nonlocal moves
            moves += abs(l) + abs(r)
            return l + r + node.val - 1
        
        moves = 0
        dfs(root)
        return moves

s = Solution()
print(s.distributeCoins(make([3,0,0])))
print(s.distributeCoins(make([0,3,0])))
print(s.distributeCoins(make([1,0,2])))
print(s.distributeCoins(make([1,0,0,None,3])))
