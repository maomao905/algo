"""
two pointers
max(left) <= min(right)

O(N)
"""
from typing import List
class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        def find_boundary(s):
            r = s
            mx = max(A[:r])
            for i in range(s,N):
                if A[i] < mx:
                    mx = max(max(A[r:i+1]), mx)
                    r = i+1
            return r
            
        N=len(A)
        for r in reversed(range(1,N)):
            if A[0] > A[r]:
                return find_boundary(r+1)
            
        return 1

"""
simpler solution

pre-compute left max and right min
return first index that satisfy left_max <= right_min
"""
class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        N=len(A)
        left_max = [A[0]] * N
        for i in range(1,N):
            left_max[i] = max(left_max[i-1], A[i])
        
        right_min = [A[-1]] * N
        for i in reversed(range(N-1)):
            right_min[i] = min(right_min[i+1], A[i])
        
        for i in range(N-1):
            if left_max[i] <= right_min[i+1]:
                return i+1
        

s = Solution()
print(s.partitionDisjoint([5,0,3,8,6]))
print(s.partitionDisjoint([1,1,1,0,6,12]))
print(s.partitionDisjoint([1,1,1,0,6,1,12]))
print(s.partitionDisjoint([2,2,2]))
print(s.partitionDisjoint([26,51,40,58,42,76,30,48,79,91]))
print(s.partitionDisjoint([32,57,24,19,0,24,49,67,87,87]))
print(s.partitionDisjoint([3,1,8,3,9,7,12,0,0,12,6,12,19]))
            
            
