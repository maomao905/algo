# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
BFS
    add children to queue and increment the depth at each level
recursive
    not good, because it all gets down to the leaf
    we want to stop at the min depth
time: O(N)
    - balanced tree, except for the bottom level(N/2), we visit all nodes -> O(N/2) = O(N)
space: same as time O(N)
"""
from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        q = deque([(1, root)])
        while len(q) > 0:
            depth, node = q.popleft()
            children = [node.left, node.right]
            # if node is leaf
            if not any(children):
                return depth
            
            for c in children:
                if c:
                    q.append((depth+1, c))
            
