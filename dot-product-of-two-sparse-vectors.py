"""
time: initialize O(M+N), dotProduct O(min(P,Q)) P: num of non-zeros in M, Q: num of non-zeros in N
space: O(P+Q)
"""

from typing import List
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = {i: nums[i] for i in range(len(nums)) if nums[i]}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        smaller = larger = None
        if len(self.nums) < len(vec.nums):
            smaller = self.nums
            larger = vec.nums
        else:
            smaller = vec.nums
            larger = self.nums
            
        return sum([n * larger.get(i, 0) for i, n in smaller.items()])

n1 = SparseVector([1,0,0,2,3])
n2 = SparseVector([0,3,0,4,0])
print(n1.dotProduct(n2))
n1 = SparseVector([0,1,0,0,0])
n2 = SparseVector([0,0,0,0,2])
print(n1.dotProduct(n2))
n1 = SparseVector([0,1,0,0,2,0,0])
n2 = SparseVector([1,0,0,0,3,0,4])
print(n1.dotProduct(n2))

        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
