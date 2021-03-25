"""
M(k-2) + k 
M(k-1)

M(-1) = M(-2) = 0
0 M(-2) + 3 or M(-1) = 3 or 0 = 3
1 M(-1) + (2 + 3) or M(0) = 5 or 3 = 5
2 M(0) + (3 + 1) or M(1) = 7 or 5 = 7

BFS to get the sum of the level -> it does not work

rob this node or not?

rob = node.val + rob(node.left, parent_robbed=True) + rob(node.right, parent_robbed=False)

not_rob = rob(node.left, parent_robbed=False) + rob(node.right, parent_robbed=False)

return max(rob, not_rob)

time: O(N)
space: O(logN), O(N) in worst
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(node, parent_robbed):
            if node is None:
                return 0
            
            robbed = 0
            if not parent_robbed:
                if (node, True) in memo:
                    robbed = memo[(node, True)]
                else:
                    robbed = node.val + dfs(node.left, True) + dfs(node.right, True)
                    memo[(node, True)] = robbed
            
            not_robbed = 0
            if (node, False) in memo:
                not_robbed = memo[(node, False)]
            else:
                not_robbed = dfs(node.left, False) + dfs(node.right, False)
                memo[(node, False)] = not_robbed
            
            return max(robbed, not_robbed)
        
        memo = {}
        return max(dfs(root, True), dfs(root, False))

"""
DP table
- how to access child robbed amount because dp table is array
    build parent - child relationship graph
    - we have to store the index of each node

dp_robbed[i] = dp_not_robbed[i_left] + dp_not_robbed[i_right]
dp_not_robbed[i] = dp_not_robbed[i_left] + dp_not_robbed[i_right] + dp_robbed[i_left] + dp_robbed[i_right]
it's too complicated to use dp table in tree
"""

# from collections import defaultdict
# class Solution:
#     def build_graph(root):
#         node_idx = {}
#         graph = {}
#         q = deque([root])
#         cnt = 0
#         while len(q) > 0:
#             node = q.popleft()
#             if node is None:
#                 continue
#             graph[node] = [node.left, node.right]
#             node_idx[node] = cnt
#             cnt += 1
#             q.append(node.left)
#             q.append(node.right)
# 
#         return graph, node_idx
# 
#     def rob(self, root: TreeNode) -> int:
#         graph, node_idx = build_graph(root)
# 
#         dp_robbed = [0] * len(node_idx)
#         dp_not_robbed = [0] * len(node_idx)
# 
#         for in reversed(node_idx)
        
        

from collections import deque
def make(vals):
  val_q = deque(vals)
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
  return root
s = Solution()
print(s.rob(make([3,2,3,None,3,None,1])))
print(s.rob(make([3,4,5,1,3,None,1])))
print(s.rob(make([2,1,3,None,4])))
                
        
