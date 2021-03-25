"""
           0
        /      \
      1          2
     /\         /  \
    3   4      5    6
  / \  / \   / \   / \ 
 7  8 9  10 11 12 13 14

     i
   /   \
2*i+1 2*i+2
"""

class Node():
    def __init__(self, start, end):
        self.start = start # start index in the array
        self.end = end # end index in the array
        self.left = None # left subtree
        self.right = None # right subtree
        self.val = 0

class SegTree():
    # O(2N) = O(N)
    def __init__(self, arr):
        def build(l, r):
            node = Node(l, r)
            if l == r:
                node.val = arr[l]
                return node
            
            mid = l + (r-l) // 2
            node.left = build(l, mid)
            node.right = build(mid+1, r)
            
            node.val = self.merge(node.left.val, node.right.val)
            return node
        
        self.root = build(0, len(arr)-1)
    
    # O(logN)
    def update(self, i, val):
        def _update(node):
            if node.start == node.end:
                node.val = val
                return val
            
            if node.left.start <= i <= node.left.end:
                _update(node.left)
            else:
                _update(node.right)
            
            node.val = self.merge(node.left.val, node.right.val)
            return node.val
        
        return _update(self.root)
            
    
    # O(logN)
    def range(self, i, j):
        """
        sum of arr[i..j]
        """
        def _range(node, i, j):
            if node.start == i and node.end == j:
                return node.val
            
            # left subtree
            if j <= node.left.end:
                return _range(node.left, i, j)
            # right subtree
            elif node.right.start <= i:
                return _range(node.right, i, j)
            else:
                return self.merge(_range(node.left, i, node.left.end), _range(node.right, node.right.start, j))
        
        if i > j or not(self.root.start <= i and j <= self.root.end):
            raise ValueError('input start and end is out of range')
        return _range(self.root, i, j)
    
    def merge(self, x, y):
        return x + y

arr = [18, 17, 13, 19, 15, 11, 20, 12, 33, 25]
tree = SegTree(arr)
print(tree.range(2,8))
