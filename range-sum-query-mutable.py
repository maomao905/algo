"""
segment tree

init O(N)
update, sumRange O(logN)
"""
from typing import List
class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None
        self.val = 0

class NumArray:
    def __init__(self, nums: List[int]):
        def build(l, r):
            node = Node(l, r)
            if l == r:
                node.val = nums[l]
                return node
            
            mid = l + (r-l)//2
            node.left = build(l, mid)
            node.right = build(mid+1, r)
            
            node.val = self.merge(node.left.val, node.right.val)
            return node
        
        self.root = build(0, len(nums)-1)
        

    def update(self, index: int, val: int) -> None:
        def update(node):
            if node.start == node.end:
                node.val = val
                return val
            
            if node.left.start <= index <= node.left.end:
                update(node.left)
            else:
                update(node.right)
            
            node.val = self.merge(node.left.val, node.right.val)
            return node.val
            
        return update(self.root)
        

    def sumRange(self, left: int, right: int) -> int:
        def range(node, i, j):
            if node.start == i and node.end == j:
                return node.val
            
            if j <= node.left.end:
                return range(node.left, i, j)
            elif node.right.start <= i:
                return range(node.right, i, j)
            else:
                return self.merge(range(node.left, i, node.left.end), range(node.right, node.right.start, j))
        
        if left > right or not(self.root.start <= left and right <= self.root.end):
            raise ValueError('input start and end is out of range')
        
        return range(self.root, left, right)
                
    def merge(self, x, y):
        return x + y


# Your NumArray object will be instantiated and called as such:
arr = NumArray([1,3,5])
print(arr.sumRange(0, 2))
print(arr.update(1, 2))
print(arr.sumRange(0, 2))
