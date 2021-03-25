"""
sliding window
start from left (smallest value)
if window size is less than k: just append
else
    if abs(leftmost value of the window - target) < abs(current value - target)
        popleft and append
    else
        return

O(N)
"""
from collections import deque
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        def dfs(node):
            if node is None:
                return
            
            dfs(node.left)
            if len(q) == k:
                if abs(target - node.val) > abs(target - q[0]):
                    return
                q.popleft()
            
            q.append(node.val)
            dfs(node.right)
        
        q = deque()
        dfs(root)
        return list(q)
                
