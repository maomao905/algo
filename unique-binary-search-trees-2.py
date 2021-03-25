"""
n=3
root=1
    - left: <1
    - right: 1<
recursively create left and right nodes given root node

generate subtrees and generate subtrees under the subtree
return all subtrees and iterate it to connect left and right of parent node

time: Catalan number
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generate(start, end):
            if start > end:
                return [None]
            res = []
            for i in range(start, end+1):
                left_subtrees = generate(start, i-1)
                right_subtrees = generate(i+1, end)
                
                for l in left_subtrees:
                    for r in right_subtrees:
                        node = TreeNode(val=i)
                        node.left = l
                        node.right = r
                        res.append(node)
            return res
        
        if n == 0:
            return []
        return generate(1, n)

s = Solution()
print(s.generateTrees(3))
print(s.generateTrees(0))
