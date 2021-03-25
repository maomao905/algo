"""
DFS
keep min/max depth
0 <= left min depth - right max depth <= 1
0 <= left max depth - right min depth <= 1

O(N)
"""
from lib.Tree import *
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        ans = True
        def dfs(node, is_right):
            if node is None:
                return (0, 0)
            l_min, l_max = dfs(node.left, False)
            r_min, r_max = dfs(node.right, is_right)
            nonlocal ans
            ans &= 0 <= l_max - r_min <= 1 and 0 <= l_min - r_max <= 1
            return (min(l_min, r_min)+1, max(l_max, r_max)+1)
        dfs(root, True)
        return ans

"""
DFS

     n
   /   \
 2*n  2*n+1

if we fill value like above starting from root node as 1, last leaf node value should be len(nodes)

O(N)
"""

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        mx = 0
        cnt = 0
        def dfs(node, val=1):
            if node is None:
                return
            
            nonlocal cnt, mx
            cnt += 1
            mx = max(mx, val)
            
            dfs(node.left, val<<1)
            dfs(node.right, (val<<1) + 1)
        
        dfs(root)
        return mx == cnt

            
s = Solution()
print(s.isCompleteTree(make([1,2,3,4,5,6,7])))
print(s.isCompleteTree(make([1,2,3,4,5,None,7])))
print(s.isCompleteTree(make([1,2,3,5])))
