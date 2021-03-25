"""
merge sort
count how many times the elements move left to get larger nums than self
  [1,3,3,3,2,4,2,1,2]
  [1,3,3,3,2][4,2,1,2]
  [1,3,3][3,2][4,2][1,2]
 [1,3][3][3,2][4,2][1,2]
[1][3][3][3][2][4][2][1][2]
 [1,3][3][2,3][2,4][1,2]
 [1,3,3][2,3][2,4][1,2]
  [1,2,3,3,3][1,2,2,4]
  [1,1,2,2,2,3,3,3,4]
 
merge sort in reverse order
count how many times the elements move right to get smaller nums than self
   [2,1,2,4,2,3,3,3,1]
   [2,1,2,4,2][3,3,3,1]
  [2,1][2,4,2][3,3][3,1]
 [2,1][2,4][2][3,3][3,1]
[2][1][2][4][2][3][3][3][1]
  [1,2][2,4][2][3,3][1,3]
  [1,2][2,2,4][3,3][1,3]
  [1,2,2,2,4][1,3,3,3]
  [1,1,2,2,2,3,3,3,4]

stable sort (same number stays)
O(NlogN)
"""
from typing import List

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        def sort_larger(arr, l, r):
            # only one element
            if l==r:
                return
            
            mid = l+(r-l)//2
            sort_larger(arr, l, mid)
            sort_larger(arr, mid+1, r)
            merge_larger(arr, l, r, mid)
        
        """
        merge [l..mid] and [mid+1..r]
        """
        def merge_larger(arr, l, r, mid):
            i = l
            j = mid+1
            k = l
            
            while i <= mid and j <= r:
                if arr[i][0] <= arr[j][0]:
                    temp[k] = arr[i]
                    k += 1
                    i += 1
                else:
                    # right element moves to left
                    temp[k] = arr[j]
                    larger[arr[j][1]] += mid - i + 1
                    k += 1
                    j += 1
            
            while i <= mid:
                temp[k] = arr[i]
                k += 1
                i += 1
            
            while j <= r:
                temp[k] = arr[j]
                larger[arr[j][1]] += mid - i + 1
                k += 1
                j += 1
            
            for i in range(l, r+1):
                arr[i] = temp[i]
                    
        def sort_smaller(arr, l, r):
            if l==r:
                return
            mid = l+(r-l)//2
            # print(arr,l,r)
            sort_smaller(arr, mid+1, r)
            sort_smaller(arr, l, mid)
            merge_smaller(arr, l, r, mid)
        
        """
        move greater element from left to right
        """
        def merge_smaller(arr, l, r, mid):
            i, j = mid, r
            k = r
            
            while l <= i and mid+1 <= j:
                if arr[i][0] <= arr[j][0]:
                    temp[k] = arr[j]
                    k -= 1
                    j -= 1
                else:
                    # move right
                    temp[k] = arr[i]
                    smaller[arr[i][1]] += j - (mid+1) + 1
                    k -= 1
                    i -= 1
            
            while mid+1 <= j:
                temp[k] = arr[j]
                k -= 1
                j -= 1
                
            while 0 <= i:
                temp[k] = arr[i]
                smaller[arr[i][1]] += j - (mid+1) + 1
                k -= 1
                i -= 1
            for i in range(l, r+1):
                arr[i] = temp[i]
                    
        N=len(instructions)
        MOD = 10**9+7
        
        larger, smaller = [0] * N, [0] * N
        # save the sorted array temporarily
        arr_larger = [[n, i] for i, n in enumerate(instructions)]
        arr_smaller = [[n, i] for i, n in enumerate(reversed(instructions))]
        temp = [0] * N
        sort_larger(arr_larger, 0, N-1)
        temp = [0] * N
        sort_smaller(arr_smaller, 0, N-1)
        cost = 0
        for l, s in zip(larger, reversed(smaller)):
            cost += min(l, s)
        return cost % MOD

""" 
segment tree  
O(NlogM)
           0
        /      \
      1          2
     /\         /  \
    3   4      5    6
  / \  / \   / \   / \ 
 7  8 9  10 11 12 13 14
 
if 7 is max, (7+1) * 2 = 16 length of array

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
        self.total = 0

class SegTree():
    # O(2N) = O(N)
    def __init__(self, arr):
        def build(arr, l, r):
            node = Node(l, r)
            if l == r:
                node.total = arr[l]
                return node
            
            mid = (l + r) // 2
            node.left = build(arr, l, mid)
            node.right = build(arr, mid+1, r)
            
            node.total = node.left.total + node.right.total
            return node
        
        self.root = build(arr, 0, len(arr)-1)
    
    # O(logN)
    def update(self, i, val):
        def _update(node, i, val):
            if node.start == node.end:
                node.total = val
                return val
            
            mid = node.start + (node.end - node.start)//2
            if i <= mid:
                _update(node.left, i, val)
            else:
                _update(node.right, i, val)
            
            node.total = node.left.total + node.right.total
            return node.total
        
        return _update(self.root, i, val)
            
    
    # O(logN)
    def query(self, i, j):
        """
        sum of arr[i..j]
        """
        def _query(node, i, j):
            if node.start == i and node.end == j:
                return node.total
            
            mid = node.start + (node.end - node.start)//2
            
            # left subtree
            if j <= mid:
                return _query(node.left, i, j)
            # right subtree
            elif i > mid:
                return _query(node.right, i, j)
            else:
                return _query(node.left, i, mid) + _query(node.right, mid+1, j)
        
        if i > j:
            return 0
        return _query(self.root, i, j)
                

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9+7
        m = max(instructions)+1
        tree = SegTree([0]*m)
        cost = 0
        for i, x in enumerate(instructions):
            freq = tree.query(x, x)
            tree.update(x, freq+1)
            left_cost = tree.query(0,x-1)
            right_cost = tree.query(x+1,m-1)
            cost += min(left_cost, right_cost)
        return cost % MOD

"""
Binary Indexed Tree
O(NlogM) M: max value of instructions
"""
class BIT():
    def __init__(self, nums):
        self.nums = nums
        self.N = len(nums)
        self.tree = [0] * (self.N+1)
        
    def add(self, i):
        diff, self.nums[i] = 1, self.nums[i] + 1
        i += 1
        while i <= self.N:
            self.tree[i] += diff
            i += i & -i
    
    def prefix_sum(self, i):
        _sum = 0
        i += 1
        while i:
            _sum += self.tree[i]
            i -= i & -i
        return _sum
    
    def range_sum(self, i, j):
        return self.prefix_sum(j) - self.prefix_sum(i-1)

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9+7
        m = max(instructions)+1
        tree = BIT([0]*m)
        cost = 0
        for i, x in enumerate(instructions):
            tree.add(x)
            left_cost = tree.prefix_sum(x-1)
            right_cost = i + 1 - tree.prefix_sum(x)
            cost += min(left_cost, right_cost)
        return cost % MOD

            
s = Solution()            
print(s.createSortedArray([1,5,6,2]))
print(s.createSortedArray([1,2,3,6,5,4]))
# print(s.createSortedArray([1,3,1,3,2,4,2,1,2,5,6,7]))
print(s.createSortedArray([1,3,3,3,2,4,2,1,2]))
                                 # ^
            
            
