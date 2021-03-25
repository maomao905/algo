"""
preorder traversal
encode 1,2,null,null,3,4,5
decode split string by , and pop top of the list and preorder traversal
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node):
            if node is None:
                return ['null']
            
            res = []
            res.append(str(node.val))
            res.extend(dfs(node.left))
            res.extend(dfs(node.right))
            return res
        
        return ','.join(dfs(root))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = deque(data.split(','))
        
        def dfs():
            s = nodes.popleft()
            if s == 'null':
                return None
            
            node = TreeNode(int(s))
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()
            
        
from lib.Tree import *
# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
encoded = ser.serialize(make([1,2,3,None,None,4,5]))
print(encoded)
print(show(deser.deserialize(encoded)))
