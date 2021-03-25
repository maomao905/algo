"""
return count, value to root node
add count when the returned value and node value is the same
path count = (left count + 1) + (right count + 1) +1 means adding edge count
update max count

dfs post-order traversal (left -> right -> root)

  count  value
1  0      1
1  0      1
4  0      4
5  0      5
5  1      5
5  2      5 -> 2 is max
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from lib.Tree import *

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        max_cnt = 0
        def post_order(node):
            nonlocal max_cnt
            if node is None:
                return 0, None
            l_cnt, l_val = post_order(node.left)
            r_cnt, r_val = post_order(node.right)
            
            cnt = 0
            new_l_cnt = new_r_cnt = 0
            if l_val == node.val:
                new_l_cnt = l_cnt + 1
                cnt = l_cnt
            
            if r_val == node.val:
                new_r_cnt = r_cnt + 1
                cnt = max(cnt, r_cnt)
            
            # the problem is not clearly stated
            max_cnt = max(max_cnt, new_l_cnt + new_r_cnt)
            return max(new_l_cnt, new_r_cnt), node.val
        
        post_order(root)
        return max_cnt
        
        

s = Solution()
print(s.longestUnivaluePath(make([5,4,5,1,1,5])))
print(s.longestUnivaluePath(make([1,4,5,4,4,5])))
print(s.longestUnivaluePath(make([1,None,1,1,1,1,1,1])))
