"""
all of them use DFS
pre-order
in-order
    - left -> root -> right
post-order
"""
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(node):
            if node is None:
                return
            
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)
        
        ans = []
        dfs(root)
        return ans

"""
use stack
1. push left node as long as it exists
2. if there is no left node, pop from stack and go to right
    - while looking left, it also include the root(parent) node
        so, we don't need to push root(parent) node
time and space: O(N)
"""
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        cur = root
        res = []
        while cur or len(stack) > 0:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            node = stack.pop()
            res.append(node.val)
            cur = node.right
        return res
                

from collections import deque
val_q = deque([1,None,2,3])
root = TreeNode(val=val_q.popleft())
node_q = deque([root])

while len(val_q) > 0:
    node = node_q.popleft()
    
    left = val_q.popleft()
    if left:
        node.left = TreeNode(val=left)
    
    if len(val_q) > 0:
        right = val_q.popleft()
        if right:
            node.right = TreeNode(val=right)
    
    if node.left:
        node_q.append(node.left)
    if node.right:
        node_q.append(node.right)

s = Solution()        
print(s.inorderTraversal(root))
