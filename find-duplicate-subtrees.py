"""
store path in set in string
if it matches, store the root node

post order traversal
4
4L2
4
4L2
4
4L2L4R3

O(N^2)
"""
from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        def dfs(node):
            path = ''
            if node.left:
                path += dfs(node.left) + 'L'
            if node.right:
                path += dfs(node.right) + 'R'
            
            path += str(node.val)
            if path in seen:
                res.add(seen[path])
            else:
                seen[path] = node
            
            return path
        
        res = set()
        seen = {}
        
        dfs(root)
        return list(res)
            
"""
use int instead of string as id, thus it takes constant time to hash
time O(N) space O(N)
"""
from collections import defaultdict, Counter
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        ids = defaultdict()
        ids.default_factory = ids.__len__
        cnt = Counter()
        
        def lookup(node):
            if node:
                uid = ids[node.val, lookup(node.left), lookup(node.right)]
                cnt[uid] += 1
                if cnt[uid] == 2:
                    res.append(node)
                return uid
        
        res = []
        lookup(root)
        return res
